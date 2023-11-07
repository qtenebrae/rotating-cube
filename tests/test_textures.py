import pytest
from unittest.mock import Mock
import moderngl as mgl
from src.textures import Textures


@pytest.fixture
def mock_app():
    mock_app = Mock()
    mock_app.ctx = Mock()
    return mock_app


def test_textures_initialization(mock_app):
    # Проверяем инициализацию класса Textures
    textures = Textures(mock_app)

    assert textures.app == mock_app
    assert textures.ctx == mock_app.ctx
    assert len(textures.textures) == 6


def test_texture_loading(mock_app):
    # Проверяем загрузку текстур
    textures = Textures(mock_app)

    for texture in textures.textures:
        assert texture.filter == (mgl.NEAREST, mgl.NEAREST)
        assert texture.anisotropy == 32.0
        assert texture.build_mipmaps_called
        assert texture.use_called


def test_texture_loading_with_invalid_file(mock_app):
    # Проверяем поведение при загрузке недопустимого файла
    textures = Textures(mock_app)

    with pytest.raises(Exception):
        textures.load('invalid_texture.jpg')


def test_texture_loading_with_invalid_file_extension(mock_app):
    # Проверяем поведение при загрузке файла с недопустимым расширением
    textures = Textures(mock_app)

    with pytest.raises(Exception):
        textures.load('texture.docx')
