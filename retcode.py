class RETCODE:
    SUCCESS = 0  # 成功
    PARAM_REQUIRED = -246  # 需要参数
    FAILED = -247  # 失败
    TOO_LONG = -248  # 过长（用户名或其他参数）
    TOO_SHORT = -249  # 过短（用户名或其他参数）
    INVALID_PARAMS = -250  # 非法参数
    ALREADY_EXISTS = -251  # 已经存在
    NOT_FOUND = -252  # 未找到
    UNKNOWN = -253  # 未知错误
    NOT_USER = -254  # 未登录
    ROLE_REQUEST_FAILED = -246  # 权限申请失败
    PERMISSION_DENIED = -255  # 无权访问