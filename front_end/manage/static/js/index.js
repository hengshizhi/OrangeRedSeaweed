function modlist_refresh(){
    function htmladd(mod_name,url){
        return `<li class="nav-item">
        <a class="nav-link has-arrow " href="`+url+`">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-package nav-icon icon-xs me-2"><line x1="16.5" y1="9.4" x2="7.5" y2="4.21"></line><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg><font _mstmutation="1" _msttexthash="5055388" _msthash="15">`+mod_name+`</font></a>
        </li>`
    }
    // 自定义成功回调函数
    function handleSuccess(response) {
        $(function(){
            con = ''
            response = JSON.parse(response)
            for(var pl in response){
                con += htmladd(pl,'#')
            }
            $("#Plugin-Settings").html(con);
        })
    }
    
    // 自定义失败回调函数
    function handleError(xhr, status, error) {
        // console.log('API请求失败！');
        // console.log('错误状态：', status);
        // console.log('错误信息：', error);
        modlist_refresh()
    }
    
    // 调用API请求
    var apiUrl = '/api/mod?ModName=mod&ApiName=Modlist';
    var requestData = {};
    
    _sendAPIRequest(apiUrl, requestData, handleSuccess, handleError);
}
function main(){
    modlist_refresh()
}
main()