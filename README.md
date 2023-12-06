**Deployments**

[![pages](https://github.com/thevickypedia/pystream/actions/workflows/pages/pages-build-deployment/badge.svg)][gha_pages]
[![pypi](https://github.com/thevickypedia/pystream/actions/workflows/python-publish.yml/badge.svg)][gha_pypi]

[![PyPI version shields.io](https://img.shields.io/pypi/v/stream-localhost)][pypi]
[![Pypi-format](https://img.shields.io/pypi/format/stream-localhost)](https://pypi.org/project/stream-localhost/#files)
[![Pypi-status](https://img.shields.io/pypi/status/stream-localhost)][pypi]

# Video Streaming
Python module to, stream videos via authenticated sessions using FastAPI

## Install
```shell
python -m pip install stream-localhost
```

## Usage
```python
import os
import pystream

if __name__ == '__main__':
    kwargs = dict(
        username="foo",
        password="bar",
        video_source=os.path.join(os.path.expanduser('~'), 'Downloads'),
    )
    # Add the following to host on local IP address, skip for localhost (127.0.0.1)
    kwargs["video_host"] = pystream.utils.get_local_ip()
    pystream.start(**kwargs)
```

### Env Variables
> Environment variables can be loaded from any file. Defaults to `.env` (_set the env var `env_file` to the filename_)

**Mandatory**
- **USERNAME**: Any username of choice.
- **PASSWORD**: Any password of choice.
- **VIDEO_SOURCE**: Source path for `.mp4` files.

**Optional**
- **VIDEO_HOST**: IP address to host the video. Defaults to `127.0.0.1`
- **VIDEO_PORT**: Port number to host the application. Defaults to `8000`
- **WORKERS**: Number of workers to spin up the `uvicorn` server. Defaults to `1`
- **WEBSITE**: Website to add to CORS configuration. _Required only if tunneled via CDN_
- **AUTO_THUMBNAIL**: Boolean flag to auto generate thumbnail images for preview. Defaults to `True`
- **SCAN_INTERVAL**: Interval in seconds to deep scan `VIDEO_SOURCE` for `.mp4` files. Defaults to `30s`, set to `0` to skip

## Coding Standards
Docstring format: [`Google`][google-docs] <br>
Styling conventions: [`PEP 8`][pep8] and [`isort`][isort]

## [Release Notes][release-notes]
**Requirement**
```shell
python -m pip install gitverse
```

**Usage**
```shell
gitverse-release reverse -f release_notes.rst -t 'Release Notes'
```

## Linting
`pre-commit` will ensure linting, run pytest, generate runbook & release notes, and validate hyperlinks in ALL
markdown files (including Wiki pages)

**Requirement**
```shell
pip install sphinx==5.1.1 pre-commit recommonmark
```

**Usage**
```shell
pre-commit run --all-files
```

## Pypi Package
[![pypi-module](https://img.shields.io/badge/Software%20Repository-pypi-1f425f.svg)][pypi-repo]

[https://pypi.org/project/stream-localhost/][pypi]

## Runbook
[![made-with-sphinx-doc](https://img.shields.io/badge/Code%20Docs-Sphinx-1f425f.svg)][sphinx]

[https://thevickypedia.github.io/pystream/][runbook]

## License & copyright

&copy; Vignesh Rao

Licensed under the [MIT License][license]

[license]: https://github.com/thevickypedia/pystream/blob/master/LICENSE
[pypi]: https://pypi.org/project/stream-localhost
[pypi-repo]: https://packaging.python.org/tutorials/packaging-projects/
[release-notes]: https://github.com/thevickypedia/pystream/blob/master/release_notes.rst
[gha_pages]: https://github.com/thevickypedia/pystream/actions/workflows/pages/pages-build-deployment
[gha_pypi]: https://github.com/thevickypedia/pystream/actions/workflows/python-publish.yml
[google-docs]: https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
[pep8]: https://www.python.org/dev/peps/pep-0008/
[isort]: https://pycqa.github.io/isort/
[sphinx]: https://www.sphinx-doc.org/en/master/man/sphinx-autogen.html
[runbook]: https://thevickypedia.github.io/pystream/
