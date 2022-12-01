from pathlib import Path

import testloop
from poetry_publish.publish import poetry_publish


def publish():
    poetry_publish(
        package_root=Path(testloop.__file__).parent.parent,
        version=testloop.__version__,
    )
