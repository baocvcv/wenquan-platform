module.exports = {
  outputDir: "dist",
  assetsDir: "static",
  publicPath: "",
  devServer: {
    port: 80, //port
    disableHostCheck: true, //disable host headers check
	/*proxy: {
	  "/smmsImageUpload": {
		  target: "https://sm.ms/api/upload",
		  changeOrigin: true,
		  pathRewrite: {
			"^/smmsImageUpload": ""
		  }
	  }
	}*/	
  },
  lintOnSave: false //cancel output of eslint
};
