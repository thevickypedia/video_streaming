import os
from collections.abc import Generator

from pystream.models import config


def get_stream_files() -> Generator[os.PathLike]:
    """Get files to be streamed.

    Yields:
        Path for video files.
    """
    for __path, __directory, __file in os.walk(config.env.video_source):
        if __path.endswith('__'):
            continue
        for file_ in __file:
            if file_.startswith('__'):
                continue
            if file_.endswith('.mp4'):
                path = __path.replace(str(config.env.video_source), "")
                if not path:
                    value = os.path.join(config.static.VAULT, file_)
                elif path.startswith("/"):
                    value = config.static.VAULT + path + os.path.sep + file_
                else:
                    value = config.static.VAULT + os.path.sep + path + os.path.sep + file_
                yield value