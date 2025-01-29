## 1. Loading a pickle file

```with open('data.pkl', 'rb',, buffering=1024 * 1024) as input_model:
  model_object = dill.load(input_model)
  model_object = dill.dump(model_object, input_model, protocol=dill.HIGHEST_PROTOCOL)

Why? The default buffer size is small, increasing it reduces disk read time.
Try 1MB (1024*1024) or higher based on your system performance.

protocol --- This ensures that the file is stored in an optimized binary format for quicker deserialization.
```

