function get(keyword) {
    var reg = new RegExp("(^|&)" + keyword + "=([^&]*)(&|$)", "i");
    var r = window.location.search.substr(1).match(reg);
    if (r != null) return unescape(r[2]);
    return null;   //注意此处参数是中文，解码使用的方法是unescape ，那么在传值的时候如果是中文，需要使用escape('曲浩')方法来编码。
}

class Lci_user {
    RURL = '';
    OtherData = '';
    OtherID = '';
    OtherKey = '';
    SessionKey = null;

    reqapi(name, parameter, Call = function (data) {
        console.log(data)
    }) {
        // 请求API
        // name :API名字
        // parameter :参数
        // Call :请求后执行的函数,传入返回内容
        console.log(this.RURL + name);
        let url = this.RURL + name;
        parameter['SessionKey'] = this.SessionKey;
        $(function () {
            $.ajax({
                type: "GET",
                url: url,
                data: parameter,
                success: function (data) {
                    Call(data)
                    console.log(data);
                }
            });
        });
    }

    constructor(Lci_user_url = '/api/', SessionKey) {
        this.RURL = Lci_user_url;
        if (SessionKey == null) {
            this.SessionKey = $.cookie('SessionKey');
            ;
            if (this.SessionKey == null) {
                $(function () {
                    $.ajax({
                        type: "GET",
                        url: Lci_user_url + 'Get_session_key', //拼接接口地址
                        data: {},
                        success: function (data) {
                            $.cookie('SessionKey', data);
                            console.log(data);
                        }
                    });
                });
                // this.SessionKey = this.reqapi('Get_session_key',{})
            }
        }
    }

    signup(name, Key, nickname, postbox = None, Call = function (data) {
        console.log(data)
    }) {
        `
        注册:
        name 用户名
        key 密码(几乎没用)
        nickname 昵称
        postbox 邮箱(必须要)
        `
        if (postbox == None) {
            return 'The mailbox cannot be empty'
        }
        return this.reqapi('registered', {
            name: name,
            Key: Key,
            postbox: postbox,
            nickname: nickname,
        }, Call)
    }

    logon(id = null, name = null, postbox = null, Call = function (data) {
        console.log(data)
    }) {
        // 登录
        return this.reqapi('login_SendEmainVerification_API', {
                user_id: id,
                user_name: name,
                postbox: postbox,
            }, Call
        )
    }

    logonValidate(ValidateCode = null, Call = function (data) {
        console.log(data)
    }) {
        // 登录，验证验证码是否正确
        return this.reqapi('login_Email_Verifier_API', {
                Verification: ValidateCode,
            }, Call
        )
    }

    LoginStatus(Call = function (data) {
        console.log(data)
    }) {
        // 获取登录状态
        return this.reqapi('login_status', {}, Call
        )
    }
}