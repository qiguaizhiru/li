#!/usr/bin/env python3
"""
FC26 Custom Player Mod Installer - 骆歆 (Luo Xin)
==================================================
将骆歆的自定义球员数据安装到 EA SPORTS FC 26 中。

使用方法:
    python install.py --game-path "C:/Program Files/EA SPORTS FC 26"

依赖工具:
    - FIFA Editor Tool (FET) 或 RDBM Tool (用于编辑数据库)
    - Frosty Mod Manager (用于打包和加载mod)
"""

import json
import os
import sys
import shutil
import argparse
from pathlib import Path


def load_player_config(config_path: str) -> dict:
    """加载球员配置文件"""
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def validate_game_path(game_path: str) -> bool:
    """验证游戏安装路径"""
    game_dir = Path(game_path)
    if not game_dir.exists():
        print(f"[错误] 游戏路径不存在: {game_path}")
        return False
    # 检查关键游戏文件
    expected_files = ["fc26.exe", "Data"]
    for f in expected_files:
        if not (game_dir / f).exists():
            print(f"[警告] 未找到预期文件/目录: {f}")
    return True


def generate_frosty_mod(player_config: dict, output_dir: str) -> str:
    """
    生成 Frosty Mod Manager 兼容的mod文件结构。
    实际的 .fbmod 文件需要通过 Frosty Editor 创建，
    这里生成中间配置文件供编辑器导入。
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    mod_config = {
        "ModDetails": {
            "Title": player_config["mod_info"]["name"],
            "Author": player_config["mod_info"]["author"],
            "Version": player_config["mod_info"]["version"],
            "Description": player_config["mod_info"]["description"],
            "GameVersion": "FC26"
        },
        "PlayerData": {
            "Name": player_config["player"]["basic_info"]["name_en"],
            "NameCN": player_config["player"]["basic_info"]["name_cn"],
            "Overall": player_config["player"]["attributes"]["overall_rating"],
            "Position": player_config["player"]["basic_info"]["position_primary"],
            "Nationality": player_config["player"]["basic_info"]["nationality"],
            "Height": player_config["player"]["basic_info"]["height_cm"],
            "Weight": player_config["player"]["basic_info"]["weight_kg"],
            "PreferredFoot": player_config["player"]["basic_info"]["preferred_foot"],
            "WeakFoot": player_config["player"]["basic_info"]["weak_foot_stars"],
            "SkillMoves": player_config["player"]["basic_info"]["skill_moves_stars"],
            "Attributes": player_config["player"]["attributes"],
            "PlayStyles": player_config["player"]["playstyle"],
            "Traits": player_config["player"]["traits"]
        },
        "Appearance": player_config["player"]["appearance"],
        "TeamAssignment": player_config["team_assignment"]
    }

    mod_file = output_path / "luoxin_fc26_mod.json"
    with open(mod_file, 'w', encoding='utf-8') as f:
        json.dump(mod_config, f, ensure_ascii=False, indent=2)

    print(f"[成功] Mod配置已生成: {mod_file}")
    return str(mod_file)


def generate_lua_script(player_config: dict, output_dir: str) -> str:
    """
    生成 FIFA Editor Tool (FET) 的 Lua 脚本，
    用于将球员数据直接写入游戏数据库。
    """
    player = player_config["player"]
    info = player["basic_info"]
    attrs = player["attributes"]
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    lua_script = f'''-- ============================================
-- FC26 Custom Player Mod - {info["name_cn"]} ({info["name_en"]})
-- 英雄联盟主持人骆歆的自定义球员
-- 使用 FIFA Editor Tool (FET) 执行此脚本
-- ============================================

local playerName = "{info["name_en"]}"
local playerNameCN = "{info["name_cn"]}"

-- 创建新球员记录
local newPlayerID = CreatePlayer()

-- 基本信息
SetPlayerInfo(newPlayerID, "firstname", "Xin")
SetPlayerInfo(newPlayerID, "surname", "Luo")
SetPlayerInfo(newPlayerID, "commonname", "{info["short_name"]}")
SetPlayerInfo(newPlayerID, "nationality", 155)  -- China
SetPlayerInfo(newPlayerID, "height", {info["height_cm"]})
SetPlayerInfo(newPlayerID, "weight", {info["weight_kg"]})
SetPlayerInfo(newPlayerID, "preferredfoot", 1)  -- Right
SetPlayerInfo(newPlayerID, "weakfootabilitytypecode", {info["weak_foot_stars"]})
SetPlayerInfo(newPlayerID, "skillmoves", {info["skill_moves_stars"]})
SetPlayerInfo(newPlayerID, "preferredposition1", 18)  -- CAM
SetPlayerInfo(newPlayerID, "jerseynumber", {info["jersey_number"]})

-- 能力值设置
-- 速度 (Pace)
SetPlayerAttribute(newPlayerID, "acceleration", {attrs["pace"]["acceleration"]})
SetPlayerAttribute(newPlayerID, "sprintspeed", {attrs["pace"]["sprint_speed"]})

-- 射门 (Shooting)
SetPlayerAttribute(newPlayerID, "positioning", {attrs["shooting"]["positioning"]})
SetPlayerAttribute(newPlayerID, "finishing", {attrs["shooting"]["finishing"]})
SetPlayerAttribute(newPlayerID, "shotpower", {attrs["shooting"]["shot_power"]})
SetPlayerAttribute(newPlayerID, "longshots", {attrs["shooting"]["long_shots"]})
SetPlayerAttribute(newPlayerID, "volleys", {attrs["shooting"]["volleys"]})
SetPlayerAttribute(newPlayerID, "penalties", {attrs["shooting"]["penalties"]})

-- 传球 (Passing)
SetPlayerAttribute(newPlayerID, "vision", {attrs["passing"]["vision"]})
SetPlayerAttribute(newPlayerID, "crossing", {attrs["passing"]["crossing"]})
SetPlayerAttribute(newPlayerID, "freekickaccuracy", {attrs["passing"]["free_kick_accuracy"]})
SetPlayerAttribute(newPlayerID, "shortpassing", {attrs["passing"]["short_passing"]})
SetPlayerAttribute(newPlayerID, "longpassing", {attrs["passing"]["long_passing"]})
SetPlayerAttribute(newPlayerID, "curve", {attrs["passing"]["curve"]})

-- 盘带 (Dribbling)
SetPlayerAttribute(newPlayerID, "agility", {attrs["dribbling"]["agility"]})
SetPlayerAttribute(newPlayerID, "balance", {attrs["dribbling"]["balance"]})
SetPlayerAttribute(newPlayerID, "reactions", {attrs["dribbling"]["reactions"]})
SetPlayerAttribute(newPlayerID, "ballcontrol", {attrs["dribbling"]["ball_control"]})
SetPlayerAttribute(newPlayerID, "dribbling", {attrs["dribbling"]["dribbling"]})
SetPlayerAttribute(newPlayerID, "composure", {attrs["dribbling"]["composure"]})

-- 防守 (Defending)
SetPlayerAttribute(newPlayerID, "interceptions", {attrs["defending"]["interceptions"]})
SetPlayerAttribute(newPlayerID, "headingaccuracy", {attrs["defending"]["heading_accuracy"]})
SetPlayerAttribute(newPlayerID, "defawareness", {attrs["defending"]["def_awareness"]})
SetPlayerAttribute(newPlayerID, "standingtackle", {attrs["defending"]["standing_tackle"]})
SetPlayerAttribute(newPlayerID, "slidingtackle", {attrs["defending"]["sliding_tackle"]})

-- 身体 (Physicality)
SetPlayerAttribute(newPlayerID, "jumping", {attrs["physicality"]["jumping"]})
SetPlayerAttribute(newPlayerID, "stamina", {attrs["physicality"]["stamina"]})
SetPlayerAttribute(newPlayerID, "strength", {attrs["physicality"]["strength"]})
SetPlayerAttribute(newPlayerID, "aggression", {attrs["physicality"]["aggression"]})

-- 球风设置
SetPlayerPlaystyle(newPlayerID, "Incisive Pass", true)
SetPlayerPlaystyle(newPlayerID, "Tiki Taka", true)
SetPlayerPlaystyle(newPlayerID, "Technical", true)
SetPlayerPlaystylePlus(newPlayerID, "Playmaker", true)

-- 特性设置
SetPlayerTrait(newPlayerID, "Leadership", true)
SetPlayerTrait(newPlayerID, "Team Player", true)
SetPlayerTrait(newPlayerID, "Flair", true)
SetPlayerTrait(newPlayerID, "Outside Foot Shot", true)

-- 工作态度
SetPlayerInfo(newPlayerID, "attackingworkrate", 2)  -- High
SetPlayerInfo(newPlayerID, "defensiveworkrate", 1)  -- Medium

print("========================================")
print("球员 {info["name_cn"]} ({info["name_en"]}) 创建成功!")
print("总评: {attrs["overall_rating"]}")
print("位置: CAM (前腰)")
print("========================================")
'''

    lua_file = output_path / "create_luoxin_player.lua"
    with open(lua_file, 'w', encoding='utf-8') as f:
        f.write(lua_script)

    print(f"[成功] FET Lua脚本已生成: {lua_file}")
    return str(lua_file)


def main():
    parser = argparse.ArgumentParser(
        description="FC26 骆歆自定义球员Mod安装器"
    )
    parser.add_argument(
        "--game-path",
        type=str,
        default=None,
        help="FC26 游戏安装路径"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="./build",
        help="Mod输出目录 (默认: ./build)"
    )
    parser.add_argument(
        "--config",
        type=str,
        default=None,
        help="球员配置文件路径 (默认: config/player.json)"
    )
    args = parser.parse_args()

    # 确定配置文件路径
    script_dir = Path(__file__).parent.parent
    config_path = args.config or str(script_dir / "config" / "player.json")

    print("=" * 50)
    print("  FC26 自定义球员Mod - 骆歆 (Luo Xin)")
    print("  英雄联盟主持人骆歆专属球员mod")
    print("=" * 50)
    print()

    # 加载配置
    print("[信息] 加载球员配置...")
    player_config = load_player_config(config_path)
    player = player_config["player"]
    print(f"  球员: {player['basic_info']['name_cn']} ({player['basic_info']['name_en']})")
    print(f"  总评: {player['attributes']['overall_rating']}")
    print(f"  位置: {player['basic_info']['position_primary']}")
    print()

    # 验证游戏路径
    if args.game_path:
        print("[信息] 验证游戏路径...")
        if not validate_game_path(args.game_path):
            sys.exit(1)
        print()

    # 生成mod文件
    output_dir = Path(args.output)
    print("[信息] 生成Mod文件...")
    generate_frosty_mod(player_config, str(output_dir / "frosty"))
    generate_lua_script(player_config, str(output_dir / "fet"))
    print()

    print("=" * 50)
    print("  Mod文件生成完毕!")
    print()
    print("  安装方式:")
    print("  方式1: 使用 Frosty Mod Manager")
    print(f"    导入 {output_dir}/frosty/luoxin_fc26_mod.json")
    print()
    print("  方式2: 使用 FIFA Editor Tool (FET)")
    print(f"    执行 {output_dir}/fet/create_luoxin_player.lua")
    print("=" * 50)


if __name__ == "__main__":
    main()
