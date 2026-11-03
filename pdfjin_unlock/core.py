from pathlib import Path
from typing import Union, BinaryIO, Optional
import io
import pikepdf


def unlock_pdf(
    input_pdf: Union[str, Path, bytes, BinaryIO],
    password: str = "",
    output: Optional[Union[str, Path, BinaryIO]] = None,
) -> Union[bytes, Path]:
    """
    Decrypt and remove password security from a PDF.
    """
    if isinstance(input_pdf, (str, Path)):
        src = pikepdf.open(str(input_pdf), password=password)
    elif isinstance(input_pdf, bytes):
        src = pikepdf.open(io.BytesIO(input_pdf), password=password)
    else:
        src = pikepdf.open(input_pdf, password=password)

    with src:
        if output is None:
            buf = io.BytesIO()
            src.save(buf)
            return buf.getvalue()

        if isinstance(output, (str, Path)):
            out_path = Path(output)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            src.save(str(out_path))
            return out_path

        src.save(output)
        return output
