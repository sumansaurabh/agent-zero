import pytest
from pathlib import Path
from add_mandarin_readme.file_handler import read_readme, write_readme

def test_read_readme_exists(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    f = d / "test.md"
    content = "Hello World"
    f.write_text(content, encoding="utf-8")
    
    assert read_readme(str(f)) == content

def test_read_readme_not_found():
    with pytest.raises(FileNotFoundError):
        read_readme("non_existent_file.md")

def test_write_readme(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    f = d / "output.md"
    content = "你好世界"
    
    write_readme(str(f), content)
    
    assert f.read_text(encoding="utf-8") == content
