import nock from "nock";

nock(/.*?/)
  .post("/api/signup/", content => content.username != "fail")
  .reply(200, {
    data: { username: "yes" }
  });
