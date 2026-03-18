# FC26 自定义球员Mod - 骆歆 (Luo Xin)

> 英雄联盟主持人骆歆的专属FC26球员mod，让骆歆也能在绿茵场上驰骋！

## 球员信息

| 属性 | 值 |
|------|-----|
| 姓名 | 骆歆 (Luo Xin) |
| 总评 | 82 |
| 位置 | CAM (前腰) |
| 副位置 | CM, RW |
| 身高 | 168cm |
| 惯用脚 | 右脚 |
| 球衣号码 | 7 |

## 能力值总览

| 大项 | 评分 | 亮点 |
|------|------|------|
| 速度 (Pace) | 80 | 加速 83 |
| 射门 (Shooting) | 75 | 跑位 80 |
| 传球 (Passing) | **84** | 视野 88, 短传 86 |
| 盘带 (Dribbling) | **83** | 沉着 86, 敏捷 85 |
| 防守 (Defending) | 45 | - |
| 身体 (Physicality) | 65 | 体力 78 |

## 球风 (PlayStyles)

- Incisive Pass (精准直塞)
- Tiki Taka (短传配合)
- Technical (技术型)
- **Playmaker+** (组织核心+)

## 设计理念

骆歆作为英雄联盟知名主持人，具有出色的临场应变能力和全局观。将这些特质映射到足球场上：

- **高视野 (88)** - 对应主持人敏锐的观察力和全局把控能力
- **高沉着 (86)** - 对应直播中处变不惊的专业素养
- **高短传 (86)** - 对应优秀的沟通协调能力
- **Playmaker+ 球风** - 核心组织者，串联全队进攻

## 安装方法

### 方式一：Frosty Mod Manager（推荐）

1. 下载并安装 [Frosty Mod Manager](https://frostytoolsuite.com/)
2. 运行安装脚本生成mod文件：
   ```bash
   python scripts/install.py --output ./build
   ```
3. 打开 Frosty Mod Manager，导入生成的 `build/frosty/luoxin_fc26_mod.json`
4. 启用mod并启动游戏

### 方式二：FIFA Editor Tool (FET)

1. 下载并安装 FIFA Editor Tool
2. 运行安装脚本生成Lua脚本：
   ```bash
   python scripts/install.py --output ./build
   ```
3. 在 FET 中打开游戏数据库
4. 执行 `build/fet/create_luoxin_player.lua`
5. 保存并启动游戏

## 自定义修改

如需调整球员属性，编辑 `config/player.json` 文件，然后重新运行安装脚本即可。

## 目录结构

```
fc26-mod-luoxin/
├── config/
│   ├── player.json        # 球员属性配置
│   └── miniface.json      # 头像卡面配置
├── scripts/
│   └── install.py         # 安装脚本
├── assets/                # 素材目录（需自行添加）
│   ├── face/              # 面部贴图
│   ├── miniface/          # 小头像
│   ├── portraits/         # 肖像
│   └── badges/            # 徽章
└── README_MOD.md          # 本文件
```

## 注意事项

- 需要将你的面部照片制作为贴图放入 `assets/face/` 目录
- 推荐使用 Face Creator 工具制作3D面部模型
- mod仅供个人娱乐使用
