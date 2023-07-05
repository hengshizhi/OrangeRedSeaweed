// console.log(Lci_user.PullingOtherData());
layui.use('form', function () {
    var form = layui.form;
    form.on('submit(formDemo)', function (data) {
        Lci_users = new Lci_user();
        if (data.field['login_to_registered'] == 'login') {
            Lci_users.logon(null, null, data.field['email']);
            loginInformation.style.display = 'none';
            Verification.style.display = '';
        } else if (data.field['login_to_registered'] == 'registered') {
            Lci_users.signup(null, null, null, data.field['email']);
            loginInformation.style.display = 'none';
            Verification.style.display = '';
        } else if (data.field['Verification']) {
            let AskData = Lci_users.logonValidate(data.field['Verification']);
            if (AskData == 'Verification code error') {
                layer.msg('Verification code error')
            } else {
                location.reload();
            }
        } else if (data.field['Verification'] == null) {
            layer.msg('Please enter the verification')
        }
        console.log(data.field);
        // layer.msg(JSON.stringify(data.field));
        return false;
    });
});