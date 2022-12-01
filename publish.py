from pathlib import Path

import testloop
from poetry_publish.publish import poetry_publish


def publish():
    poetry_publish(
        package_root=Path(your_project.__file__).parent.parent,
        version=your_project.__version__,
    )
