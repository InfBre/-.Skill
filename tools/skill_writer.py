#!/usr/bin/env python3
import os
import json
from pathlib import Path

BOSSES_DIR = Path(__file__).parent.parent / "bosses"
BOSSES_DIR.mkdir(exist_ok=True)

def generate_skill(slug: str, skill_content: str) -> str:
    """
    生成老板Skill文件
    :param slug: 老板代号，用来做文件名和触发命令
    :param skill_content: 生成的Skill完整内容
    :return: 生成的文件路径
    """
    file_path = BOSSES_DIR / f"{slug}.md"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(skill_content)
    
    # 同步到OpenClaw全局技能目录
    global_skill_path = Path.home() / ".openclaw" / "skills" / f"{slug}.md"
    with open(global_skill_path, "w", encoding="utf-8") as f:
        f.write(skill_content)
    
    return str(file_path)

def list_bosses() -> list:
    """列出所有已生成的老板"""
    bosses = []
    for file in BOSSES_DIR.glob("*.md"):
        bosses.append(file.stem)
    return bosses

def delete_skill(slug: str) -> bool:
    """删除指定老板Skill（一键炒鱿鱼）"""
    file_path = BOSSES_DIR / f"{slug}.md"
    global_path = Path.home() / ".openclaw" / "skills" / f"{slug}.md"
    
    deleted = False
    if file_path.exists():
        file_path.unlink()
        deleted = True
    if global_path.exists():
        global_path.unlink()
        deleted = True
    return deleted

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python skill_writer.py <generate|list|delete> [slug] [content]")
        sys.exit(1)
    
    action = sys.argv[1]
    if action == "generate":
        if len(sys.argv) < 4:
            print("Missing slug or content")
            sys.exit(1)
        slug = sys.argv[2]
        content = sys.argv[3]
        path = generate_skill(slug, content)
        print(f"Generated skill at: {path}")
    elif action == "list":
        bosses = list_bosses()
        print("Generated bosses (一键炒鱿鱼用/delete-boss <name>)：")
        for boss in bosses:
            print(f"  - /{boss}")
    elif action == "delete":
        if len(sys.argv) < 3:
            print("Missing slug")
            sys.exit(1)
        slug = sys.argv[2]
        if delete_skill(slug):
            print(f"已炒掉老板: {slug}")
        else:
            print(f"老板 {slug} 不存在")
    else:
        print(f"Unknown action: {action}")
        sys.exit(1)
