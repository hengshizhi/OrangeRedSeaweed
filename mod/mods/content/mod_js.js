//------------------------ Content mod's modjs, authored by Xingzhi------------------------
// 请求函数：change
class content{
    constructor(SessionID){
        this.SessionID = SessionID
        if (SessionID == null){
            this.SessionID = getCookieObject()['Session_key']
        }
    }
    changeRequest(alias, Title, content, successCallback, errorCallback) {
        $.ajax({
            url: '/api/mod?ModName=content&ApiName=change',
            type: 'POST',
            data: {
                SessionID: this.SessionID,
                alias: alias,
                Title: Title,
                content: content
            },
            success: successCallback,
            error: errorCallback
        });
    }
    
    // 请求函数：ContentList
    contentListRequest(successCallback, errorCallback) {
        $.ajax({
            url: '/api/mod?ModName=content&ApiName=ContentList',
            type: 'POST',
            success: successCallback,
            error: errorCallback
        });
    }
    
    // 请求函数：GetAllContentTemplates
    getAllContentTemplatesRequest(successCallback, errorCallback) {
        $.ajax({
            url: '/api/mod?ModName=content&ApiName=GetAllContentTemplates',
            type: 'POST',
            success: successCallback,
            error: errorCallback
        });
    }
    
    // 请求函数：NewContent
    newContentRequest(alias, Title, content, successCallback, errorCallback) {
        $.ajax({
            url: '/api/mod?ModName=content&ApiName=NewContent',
            type: 'POST',
            data: {
                SessionID: this.SessionID,
                alias: alias,
                Title: Title,
                content: content
            },
            success: successCallback,
            error: errorCallback
        });
    }
    
    // 请求函数：urlapi
    urlapiRequest(url, successCallback, errorCallback) {
        $.ajax({
            url: '/api/mod?ModName=content&ApiName=urlapi',
            type: 'POST',
            data: {
                url: url
            },
            success: successCallback,
            error: errorCallback
        });
    }
    
    // 请求函数：ZUOzhEreadApi
    ZUOzhEreadApiRequest(alias, successCallback, errorCallback) {
        $.ajax({
            url: '/api/mod?ModName=content&ApiName=ZUOzhEreadApi',
            type: 'POST',
            data: {
                SessionID: this.SessionID,
                alias: alias
            },
            success: successCallback,
            error: errorCallback
        });
    }
    

}
