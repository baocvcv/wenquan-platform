import axios from "axios";

export default function (base64Images) {
  console.log("converting")
  var resultUrls = [];
  for(var i = 0; i < base64Images.length; i++) {
    var dataurl = base64Images[i];
    var arr = dataurl.split(','), mime = arr[0].match(/:(.*?);/)[1],
        bstr = atob(arr[1]), n = bstr.length, u8arr = new Uint8Array(n);
    while(n--){
        u8arr[n] = bstr.charCodeAt(n);
    }
    var file = new File([u8arr], String.fromCharCode(65 + i), {type:mime});
	console.log("Here " + i);
	console.log(file);
    axios
      .post("https://sm.ms/api/upload", {
        smfile: file
      }, {
		headers: {
			"Access-Control-Allow-Origin": "*"
		}
	  })
      .then(response => {
		console.log("success")
		console.log(response);
        resultUrls.push(response.data.url);	
      })
      .catch(error => {
		console.log("error")
		console.log(error)
        return error.code;
      })
  }
  return resultUrls;
}
