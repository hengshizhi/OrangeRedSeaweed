//------------------------ Content mod's modjs, authored by Xingzhi------------------------
// 请求函数：change
class content{
    constructor(SessionID){
        this.SessionID = SessionID
        if (SessionID == null){
            this.SessionID = getCookieObject()['Session_key']
        }
    }
    changeRequest( alias, Title, content) {
        $.ajax({
        url: '/api/mod?ModName=content&ApiName=change',
        type: 'POST',
        data: {
            SessionID: SessionID,
            alias: alias,
            Title: Title,
            content: content
        },
        success: function(response) {
            // 请求成功的处理逻辑
            console.log(response);
        },
        error: function(error) {
            // 请求失败的处理逻辑
            console.log(error);
        }
        });
    }
    
    // 请求函数：ContentList
     contentListRequest(paging, number_pages) {
        $.ajax({
        url: '/api/mod?ModName=content&ApiName=ContentList',
        type: 'POST',
        data: {
            paging: paging,
            number_pages: number_pages
        },
        success: function(response) {
            // 请求成功的处理逻辑
            console.log(response);
        },
        error: function(error) {
            // 请求失败的处理逻辑
            console.log(error);
        }
        });
    }
    
    // 请求函数：GetAllContentTemplates
     getAllContentTemplatesRequest() {
        $.ajax({
        url: '/api/mod?ModName=content&ApiName=GetAllContentTemplates',
        type: 'POST',
        success: function(response) {
            // 请求成功的处理逻辑
            console.log(response);
        },
        error: function(error) {
            // 请求失败的处理逻辑
            console.log(error);
        }
        });
    }
    
    // 请求函数：NewContent
    newContentRequest( alias, Title, content) {
        $.ajax({
        url: '/api/mod?ModName=content&ApiName=NewContent',
        type: 'POST',
        data: {
            SessionID: SessionID,
            alias: alias,
            Title: Title,
            content: content
        },
        success: function(response) {
            // 请求成功的处理逻辑
            console.log(response);
        },
        error: function(error) {
            // 请求失败的处理逻辑
            console.log(error);
        }
        });
    }
    
    // 请求函数：urlapi
    urlapiRequest(url) {
        $.ajax({
        url: '/api/mod?ModName=content&ApiName=urlapi',
        type: 'POST',
        data: {
            url: url
        },
        success: function(response) {
            // 请求成功的处理逻辑
            console.log(response);
        },
        error: function(error) {
            // 请求失败的处理逻辑
            console.log(error);
        }
        });
    }
    
    // 请求函数：ZUOzhEreadApi
    ZUOzhEreadApiRequest( alias) {
        $.ajax({
        url: '/api/mod?ModName=content&ApiName=ZUOzhEreadApi',
        type: 'POST',
        data: {
            SessionID: SessionID,
            alias: alias
        },
        success: function(response) {
            // 请求成功的处理逻辑
            console.log(response);
        },
        error: function(error) {
            // 请求失败的处理逻辑
            console.log(error);
        }
        });
    }

}
