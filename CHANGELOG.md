# Changelog

All notable changes to the Face Detection web app.

## [1.2.0] - 2026-05-15

### Changed
- **Default confidence reduced to 0.50** (was 0.90) for better crowd detection
- Updated confidence guide to reflect new default

### Fixed
- **Image orientation issue resolved** - Original images now display correctly
- Added EXIF-aware orientation correction using `PIL.ImageOps.exif_transpose()`
- Fixed upside-down/rotated images from phones and cameras

### Technical
- Added `get_corrected_orientation()` function
- EXIF metadata now properly read and applied
- Both original and result images maintain correct orientation

---

## [1.1.0] - 2026-05-15

### Fixed
- **TypeError with `use_container_width`** - Upgraded Streamlit to >=1.33.0 (now v1.57.0)
- CORS configuration warning resolved
- Updated `.streamlit/config.toml`

---

## [1.0.1] - 2026-05-15

### Fixed
- **ModuleNotFoundError: pkg_resources** - Added `setuptools==69.5.1` to requirements
- All dependencies now install correctly

### Added
- `test_imports.py` - Verify all dependencies work
- `start.sh` - One-command launcher with dependency testing
- Comprehensive documentation (QUICKSTART.md, TROUBLESHOOTING.md, HOSTING_GUIDE.md)

---

## [1.0.0] - 2026-05-15

### Added
- Initial Streamlit web interface
- Image upload functionality
- Adjustable confidence slider (0.5 - 0.99)
- Face detection with MTCNN
- Visual results with red circles
- Download button for annotated images
- Detection details panel
- Responsive layout (mobile-friendly)
- Branded with "Jan Steinhauer"

### Features
- Real-time face detection
- Auto-rotation for best detection
- Cached model loading for better performance
- Support for JPG, JPEG, PNG formats

---

## Configuration

**Current Versions:**
- Python: 3.12
- Streamlit: 1.57.0
- TensorFlow: 2.16.1
- MTCNN: 0.1.1
- OpenCV: 4.9.0.80
- setuptools: 69.5.1

**Default Settings:**
- Detection confidence: 0.50 (optimized for crowds)
- Min confidence: 0.50
- Max confidence: 0.99
- Step: 0.05
