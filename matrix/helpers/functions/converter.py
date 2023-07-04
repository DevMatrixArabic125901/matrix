import os

from PIL import Image

from matrix.core.logger import logging
from matrix.core.managers import edit_or_reply
from matrix.helpers.functions.vidtools import take_screen_shot
from matrix.helpers.tools import fileinfo, media_type, meme_type
from matrix.helpers.utils.utils import runcmd

LOGS = logging.getLogger(__name__)


class MatrixConverter:
    async def _media_check(self, reply, dirct, file, memetype):
        if not os.path.isdir(dirct):
            os.mkdir(dirct)
        matrixfile = os.path.join(dirct, file)
        if os.path.exists(matrixfile):
            os.remove(matrixfile)
        try:
            matrixmedia = reply if os.path.exists(reply) else None
        except TypeError:
            if memetype in ["Video", "Gif"]:
                dirct = "./temp/matrixfile.mp4"
            elif memetype == "Audio":
                dirct = "./temp/matrixfile.mp3"
            matrixmedia = await reply.download_media(dirct)
        return matrixfile, matrixmedia

    async def to_image(
        self, event, reply, dirct="./temp", file="meme.png", noedits=False, rgb=False
    ):
        memetype = await meme_type(reply)
        mediatype = await media_type(reply)
        if memetype == "Document":
            return event, None
        matrixevent = (
            event
            if noedits
            else await edit_or_reply(event, "- جار التحويل يرجى الانتظار")
        )
        matrixfile, matrixmedia = await self._media_check(reply, dirct, file, memetype)
        if memetype == "Photo":
            im = Image.open(matrixmedia)
            im.save(matrixfile)
        elif memetype in ["Audio", "Voice"]:
            await runcmd(f"ffmpeg -i '{matrixmedia}' -an -c:v copy '{matrixfile}' -y")
        elif memetype in ["Round Video", "Video", "Gif"]:
            await take_screen_shot(matrixmedia, "00.00", matrixfile)
        if mediatype == "Sticker":
            if memetype == "Animated Sticker":
                matrixcmd = f"lottie_convert.py --frame 0 -if lottie -of png '{matrixmedia}' '{matrixfile}'"
                stdout, stderr = (await runcmd(matrixcmd))[:2]
                if stderr:
                    LOGS.info(stdout + stderr)
            elif memetype == "Video Sticker":
                await take_screen_shot(matrixmedia, "00.00", matrixfile)
            elif memetype == "Static Sticker":
                im = Image.open(matrixmedia)
                im.save(matrixfile)
        if matrixmedia and os.path.exists(matrixmedia):
            os.remove(matrixmedia)
        if os.path.exists(matrixfile):
            if rgb:
                img = Image.open(matrixfile)
                if img.mode != "RGB":
                    img = img.convert("RGB")
                img.save(matrixfile)
            return matrixevent, matrixfile, mediatype
        return matrixevent, None

    async def to_sticker(
        self, event, reply, dirct="./temp", file="meme.webp", noedits=False, rgb=False
    ):
        filename = os.path.join(dirct, file)
        response = await self.to_image(event, reply, noedits=noedits, rgb=rgb)
        if response[1]:
            image = Image.open(response[1])
            image.save(filename, "webp")
            os.remove(response[1])
            return response[0], filename, response[2]
        return response[0], None

    async def to_webm(
        self, event, reply, dirct="./temp", file="animate.webm", noedits=False
    ):
        memetype = await meme_type(reply)
        if memetype not in [
            "Round Video",
            "Video Sticker",
            "Gif",
            "Video",
        ]:
            return event, None
        matrixevent = (
            event
            if noedits
            else await edit_or_reply(event, "- يتم التحويل الى ملصق متحرك")
        )
        matrixfile, matrixmedia = await self._media_check(reply, dirct, file, memetype)
        media = await fileinfo(matrixmedia)
        h = media["height"]
        w = media["width"]
        w, h = (-1, 512) if h > w else (512, -1)
        await runcmd(
            f"ffmpeg -to 00:00:02.900 -i '{matrixmedia}' -vf scale={w}:{h} -c:v libvpx-vp9 -crf 30 -b:v 560k -maxrate 560k -bufsize 256k -an '{matrixfile}'"
        )  # pain
        if os.path.exists(matrixmedia):
            os.remove(matrixmedia)
        if os.path.exists(matrixfile):
            return matrixevent, matrixfile
        return matrixevent, None

    async def to_gif(
        self, event, reply, dirct="./temp", file="meme.mp4", maxsize="5M", noedits=False
    ):
        memetype = await meme_type(reply)
        mediatype = await media_type(reply)
        if memetype not in [
            "Round Video",
            "Video Sticker",
            "Animated Sticker",
            "Video",
            "Gif",
        ]:
            return event, None
        matrixevent = (
            event
            if noedits
            else await edit_or_reply(event, "- جار التحويل يرجى الانتظار")
        )
        matrixfile, matrixmedia = await self._media_check(reply, dirct, file, memetype)
        if mediatype == "Sticker":
            if memetype == "Video Sticker":
                await runcmd(f"ffmpeg -i '{matrixmedia}' -c copy '{matrixfile}'")
            elif memetype == "Animated Sticker":
                await runcmd(f"lottie_convert.py '{matrixmedia}' '{matrixfile}'")
        if matrixmedia.endswith(".gif"):
            await runcmd(
                f"ffmpeg -f gif -i '{matrixmedia}' -fs {maxsize} -an '{matrixfile}'"
            )
        else:
            await runcmd(
                f"ffmpeg -i '{matrixmedia}' -c:v libx264 -fs {maxsize} -an '{matrixfile}'"
            )
        if matrixmedia and os.path.exists(matrixmedia):
            os.remove(matrixmedia)
        if os.path.exists(matrixfile):
            return matrixevent, matrixfile
        return matrixevent, None


Convert = MatrixConverter()
