function getParam(){
    var auth_token = [38, 0, 0, 60, 93, 49, 50, 95, 25, 22, 45, 71, 47, 94, 60, 54, 45, 70];
    var salt = Array.from("RheO5PB6mfL5N3YBH45e5XuCEaWpvWUFESqTYnZk", (x) => x.charCodeAt(0));  // https://gist.github.com/lihnux/2aa4a6f5a9170974f6aa
    var xor = auth_token.map((x, i) => String.fromCharCode(x ^ salt[i]));                       // https://stackoverflow.com/questions/32937181/javascript-es6-map-multiple-arrays
    var parameter = xor.join('')
    console.log(parameter);

    return parameter;
}

Java.perform(function(){
    var WebAppInterface = Java.use("com.example.webview.WebAppInterface");
    WebAppInterface.showToast.implementation = function(toast){       
        var result = this.callcrypt(getParam());
        console.log("Flag: " + result);
        this.showToast(result);
    }
});