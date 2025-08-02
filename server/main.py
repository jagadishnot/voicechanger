from fastapi import FastAPI, File, UploadFile, Form, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from starlette.responses import FileResponse
import os
import uuid
import shutil
from typing import Optional, List
from celebrities import (
    get_all_celebrities,
    get_celebrities_by_category,
    get_celebrity_by_id,
    get_categories,
    search_celebrities
)

app = FastAPI(
    title="Celebrity Voice Changer API",
    description="API for converting voices to Indian celebrity voices",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Directory setup
UPLOAD_DIR = "uploads"
RESULT_DIR = "results"
STATIC_DIR = "static"
IMAGES_DIR = os.path.join(STATIC_DIR, "images", "celebrities")
SAMPLES_DIR = os.path.join(STATIC_DIR, "samples")

# Create directories
for directory in [UPLOAD_DIR, RESULT_DIR, STATIC_DIR, IMAGES_DIR, SAMPLES_DIR]:
    os.makedirs(directory, exist_ok=True)

# Mount static files
app.mount("/images", StaticFiles(directory=IMAGES_DIR), name="images")
app.mount("/samples", StaticFiles(directory=SAMPLES_DIR), name="samples")

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Celebrity Voice Changer API",
        "version": "2.0.0",
        "endpoints": {
            "celebrities": "/celebrities",
            "categories": "/categories",
            "convert": "/convert",
            "results": "/results/{filename}"
        }
    }

@app.get("/celebrities")
async def get_celebrities(
    category: Optional[str] = Query(None, description="Filter by category (bollywood, tollywood, kollywood, regional)"),
    search: Optional[str] = Query(None, description="Search celebrities by name or characteristics"),
    limit: Optional[int] = Query(None, description="Limit number of results")
):
    """Get all celebrities or filter by category/search"""
    try:
        if search:
            celebrities = search_celebrities(search)
        elif category:
            celebrities = get_celebrities_by_category(category)
        else:
            celebrities = get_all_celebrities()
        
        if limit:
            celebrities = celebrities[:limit]
            
        return {
            "celebrities": celebrities,
            "total": len(celebrities),
            "category": category,
            "search": search
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/categories")
async def get_celebrity_categories():
    """Get all available celebrity categories"""
    try:
        categories = get_categories()
        category_info = {
            "bollywood": {
                "name": "Bollywood",
                "description": "Hindi cinema stars",
                "count": len(get_celebrities_by_category("bollywood"))
            },
            "tollywood": {
                "name": "Tollywood",
                "description": "Telugu cinema stars",
                "count": len(get_celebrities_by_category("tollywood"))
            },
            "kollywood": {
                "name": "Kollywood",
                "description": "Tamil cinema stars",
                "count": len(get_celebrities_by_category("kollywood"))
            },
            "regional": {
                "name": "Regional",
                "description": "Other regional cinema stars",
                "count": len(get_celebrities_by_category("regional"))
            }
        }
        
        return {
            "categories": categories,
            "category_info": category_info,
            "total_celebrities": len(get_all_celebrities())
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/celebrity/{celebrity_id}")
async def get_celebrity_details(celebrity_id: str):
    """Get detailed information about a specific celebrity"""
    try:
        celebrity = get_celebrity_by_id(celebrity_id)
        if not celebrity:
            raise HTTPException(status_code=404, detail="Celebrity not found")
        return celebrity
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/preview/{celebrity_id}")
async def get_celebrity_voice_sample(celebrity_id: str):
    """Get voice sample for a specific celebrity"""
    try:
        celebrity = get_celebrity_by_id(celebrity_id)
        if not celebrity:
            raise HTTPException(status_code=404, detail="Celebrity not found")
        
        sample_path = celebrity["voice_sample"].lstrip("/")
        full_path = os.path.join(SAMPLES_DIR, f"{celebrity_id}_sample.wav")
        
        if os.path.exists(full_path):
            return FileResponse(full_path, media_type="audio/wav")
        else:
            # Return a placeholder or error
            return {"error": "Voice sample not available", "celebrity": celebrity["name"]}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/convert")
async def convert_voice(
    file: UploadFile = File(...),
    celebrity: str = Form(...)
):
    """Convert uploaded voice to celebrity voice"""
    try:
        # Validate celebrity exists
        celebrity_data = get_celebrity_by_id(celebrity)
        if not celebrity_data:
            raise HTTPException(status_code=400, detail="Invalid celebrity ID")
        
        # Validate file type
        if not file.content_type or not file.content_type.startswith('audio/'):
            raise HTTPException(status_code=400, detail="File must be an audio file")
        
        filename = f"{uuid.uuid4()}.wav"
        original_path = os.path.join(UPLOAD_DIR, filename)

        # Save uploaded file
        with open(original_path, "wb") as f:
            f.write(await file.read())

        # Simulate celebrity conversion (just copy the file for now)
        # In a real implementation, this would use AI voice conversion
        celebrity_filename = f"{celebrity}_converted_{filename}"
        celebrity_path = os.path.join(RESULT_DIR, celebrity_filename)

        shutil.copyfile(original_path, celebrity_path)

        return {
            "success": True,
            "converted": celebrity_filename,
            "celebrity": celebrity_data["name"],
            "original_filename": file.filename,
            "message": f"Voice successfully converted to {celebrity_data['name']}"
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/convert/batch")
async def convert_voice_batch(
    files: List[UploadFile] = File(...),
    celebrity: str = Form(...)
):
    """Convert multiple audio files to celebrity voice"""
    try:
        # Validate celebrity exists
        celebrity_data = get_celebrity_by_id(celebrity)
        if not celebrity_data:
            raise HTTPException(status_code=400, detail="Invalid celebrity ID")
        
        if len(files) > 10:  # Limit batch size
            raise HTTPException(status_code=400, detail="Maximum 10 files allowed per batch")
        
        results = []
        
        for file in files:
            if not file.content_type or not file.content_type.startswith('audio/'):
                continue  # Skip non-audio files
            
            filename = f"{uuid.uuid4()}.wav"
            original_path = os.path.join(UPLOAD_DIR, filename)

            with open(original_path, "wb") as f:
                f.write(await file.read())

            celebrity_filename = f"{celebrity}_converted_{filename}"
            celebrity_path = os.path.join(RESULT_DIR, celebrity_filename)
            shutil.copyfile(original_path, celebrity_path)
            
            results.append({
                "original": file.filename,
                "converted": celebrity_filename
            })
        
        return {
            "success": True,
            "celebrity": celebrity_data["name"],
            "results": results,
            "total_converted": len(results)
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/results/{filename}")
def get_audio(filename: str):
    """Get converted audio file"""
    try:
        path = os.path.join(RESULT_DIR, filename)
        if os.path.exists(path):
            return FileResponse(path, media_type="audio/wav")
        raise HTTPException(status_code=404, detail="Audio file not found")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history")
async def get_conversion_history():
    """Get conversion history (placeholder for future implementation)"""
    try:
        # This would typically fetch from a database
        # For now, return files from results directory
        result_files = []
        if os.path.exists(RESULT_DIR):
            for filename in os.listdir(RESULT_DIR):
                if filename.endswith('.wav'):
                    file_path = os.path.join(RESULT_DIR, filename)
                    file_stat = os.stat(file_path)
                    
                    # Extract celebrity name from filename
                    celebrity_name = filename.split('_converted_')[0] if '_converted_' in filename else 'unknown'
                    
                    result_files.append({
                        "filename": filename,
                        "celebrity": celebrity_name,
                        "created_at": file_stat.st_ctime,
                        "size": file_stat.st_size
                    })
        
        # Sort by creation time (newest first)
        result_files.sort(key=lambda x: x['created_at'], reverse=True)
        
        return {
            "history": result_files[:50],  # Limit to last 50 conversions
            "total": len(result_files)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
