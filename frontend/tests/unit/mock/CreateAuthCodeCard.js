import nock from "nock";

nock(/.*/)
  .post("/api/auth_code/", body => true)
  .reply(200, {
    token: "ok"
  });
