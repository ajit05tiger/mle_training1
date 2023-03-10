import mlflow

# Create nested runs
with mlflow.start_run(
    run_name="PARENT_RUN",
    description="parent",
) as parent_run:
    mlflow.log_param("parent", "yes")
    with mlflow.start_run(
        run_name="CHILD_RUN",
        description="child",
        nested=True,
    ) as child_run:
    
        mlflow.log_param("child", "yes")

    with mlflow.start_run(
        run_name="CHILD_RUN",
        description="child",
        nested=True,
    ) as child_run:
        mlflow.log_param("child", "yes")

    with mlflow.start_run(
        run_name="CHILD_RUN",
        description="child",
        nested=True,
    ) as child_run:
        mlflow.log_param("child", "yes")



print("parent run:")

print("run_id: {}".format(parent_run.info.run_id))
print("description: {}".format(parent_run.data.tags.get("mlflow.note.content")))
print("--")

# Search all child runs with a parent id
print("child runs:")
print("run_id")