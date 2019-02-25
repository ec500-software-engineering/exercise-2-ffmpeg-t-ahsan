import pytest  # pytest >= 3.9 for tmp_path
import subprocess

@pytest.fixture
def genpat(tmp_path) -> Path:
	"""
	generate test video
	"""
	vidfn = tmp_path / 'bars.avi'

	subprocess.check_call(['ffmpeg', '-v', 'warning',
'-f', 'lavfi',
'-i', 'smptebars',
'-t', 5.,
str(vidfn)])

    return vidfn
