import nock from "nock";

nock(/.*/).post("/jwt-auth/", body => {
    return body.username=="testusr" && body.password=="testpsw";
}).reply(200, {
    token: "ok"
});
nock(/.*/).post("/jwt-auth/", body => {
    return body.username!="testusr" || body.password!="testpsw";
}).reply(400, {
    token: "no"
});