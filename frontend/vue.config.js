module.exports = {
  outputDir: "dist",
  assetsDir: "static",
  publicPath: "frontend",
  devServer: {
    port: 80, //port
    disableHostCheck: true //disable host headers check
  },
  lintOnSave: false //cancel output of eslint
};
