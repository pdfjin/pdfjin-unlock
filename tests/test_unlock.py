import pytest
import io
import pikepdf
from pathlib import Path
from pdfjin_unlock.core import unlock_pdf


def test_unlock_pdf():
    pdf = pikepdf.new()
    pdf.add_blank_page()
    buf = io.BytesIO()
    pdf.save(buf, encryption=pikepdf.Encryption(owner="mypass", user="mypass", R=4))

    unlocked_bytes = unlock_pdf(buf.getvalue(), password="mypass")
    
    # Opening unlocked bytes without password should succeed
    with pikepdf.open(io.BytesIO(unlocked_bytes)) as doc:
        assert len(doc.pages) == 1
