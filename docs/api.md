# API Reference

The package is importable as `SE489MLOpsTeamArtemisIV` after running `pip install -e .`.

## `SE489MLOpsTeamArtemisIV.config`

Project-wide path constants and typed config dataclasses.

```python
from SE489MLOpsTeamArtemisIV.config import (
    PROJECT_ROOT,
    DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR,
    MODELS_DIR, REPORTS_DIR, FIGURES_DIR,
    Config, TrainingConfig, DataConfig, DEFAULT_CONFIG,
)
```

Use these constants instead of hard-coded relative paths — they resolve against the repo root regardless of the current working directory.

## `SE489MLOpsTeamArtemisIV.logging_config`

```python
from SE489MLOpsTeamArtemisIV.logging_config import setup_logging, get_logger

setup_logging(level="INFO")
logger = get_logger(__name__)
```

## `SE489MLOpsTeamArtemisIV.data`

| Function | Purpose |
|---|---|
| `load_raw(filename)` | Read CSV from `data/raw/` |
| `load_processed(filename)` | Read CSV from `data/processed/` |
| `save_processed(df, filename)` | Write CSV to `data/processed/` |
| `process_data(input_dir, output_dir)` | Raw → processed pipeline |

CLI: `python -m SE489MLOpsTeamArtemisIV.data.make_dataset [--input PATH] [--output PATH]`

## `SE489MLOpsTeamArtemisIV.features`

```python
from SE489MLOpsTeamArtemisIV.features import build_features

df_features = build_features(df_processed)
```

## `SE489MLOpsTeamArtemisIV.models`

### `BaseModel` (abstract)

Abstract interface with `fit`, `predict`, `save`, `load`. Extend this for any new estimator.

### `Model`

Reference implementation scaffold. Serializes via `joblib`.

```python
from pathlib import Path
from SE489MLOpsTeamArtemisIV.models import Model

model = Model(config={"lr": 0.01})
# model.fit(X_train, y_train)
model.save(Path("models/model.joblib"))
reloaded = Model.load(Path("models/model.joblib"))
```

## `SE489MLOpsTeamArtemisIV.evaluation`

```python
from SE489MLOpsTeamArtemisIV.evaluation import classification_report, regression_report

metrics = classification_report(y_true, y_pred)
# -> {"accuracy": ..., "precision": ..., "recall": ..., "f1": ...}
```

## `SE489MLOpsTeamArtemisIV.visualization`

```python
from SE489MLOpsTeamArtemisIV.visualization import plot_training_history, plot_confusion_matrix
```

## `SE489MLOpsTeamArtemisIV.utils`

```python
from SE489MLOpsTeamArtemisIV.utils import set_seed, save_json, load_json

set_seed(42)
```

## Training / Prediction CLIs

```bash
python -m SE489MLOpsTeamArtemisIV.train_model --epochs 100 --batch-size 64
python -m SE489MLOpsTeamArtemisIV.predict_model --model-path models/model.joblib --input data/processed/test.csv
```

## Configuration

Defaults live in `SE489MLOpsTeamArtemisIV.config.DEFAULT_CONFIG`. Override via CLI flags on the training/prediction entrypoints.

---

**TeamArtemisIV** · Version see `SE489MLOpsTeamArtemisIV.__version__`
