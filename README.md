# pairwise-stereo-phase-align

## 领域

游戏、图形与多媒体

## 主题

立体声相位对齐

## 说明

共用重采样、分段系数与总线对齐。

初始状态下 `media/stereo_phase_align.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
