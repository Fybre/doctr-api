# Copyright (C) 2021-2025, Mindee.

# This program is licensed under the Apache License 2.0.
# See LICENSE or go to <https://opensource.org/licenses/Apache-2.0> for full license details.


from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status

from app.schemas import OCRBlock, OCRIn, OCRLine, OCROut, OCRPage, OCRWord
from app.utils import get_documents, resolve_geometry, get_document
from app.vision import init_predictor

router = APIRouter()


@router.post("/", summary="Perform OCR on multiple files - don't forget trailing /")
async def perform_ocr(request: OCRIn = Depends(), files: list[UploadFile] = [File(...)]):
    """Runs docTR OCR model to analyze the input image, returns text"""
    try:
        # generator object to list
        content, filenames = await get_documents(files)
        predictor = init_predictor(request)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    out = predictor(content)

    result = out.render()

    return result

@router.post("/single/", summary="Perform OCR on single file - don't forget trailing /")
async def perform_ocr(file: UploadFile = File(...)):
    """Runs docTR OCR model to analyze the input image, returns text"""
    request = OCRIn()
    try:
        # generator object to list
        content = await get_document(file)
        predictor = init_predictor(request)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    out = predictor(content)

    result = out.render()

    return result
