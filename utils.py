def print_context_infos(context):
    print(context.version)
    print(context.pythonVer)
    print(context.master)
    print(str(context.sparkHome))
    print(str(context.sparkUser()))
    print(context.appName)
    print(context.applicationId)
    print(context.defaultParallelism)
    print(context.defaultMinPartitions)