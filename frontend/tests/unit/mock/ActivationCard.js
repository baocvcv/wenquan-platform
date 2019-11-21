import nock from "nock";

nock(/.*/)
  .get("/api/auth_code/123", body => true)
  .reply(200, {
    token: "ok"
  });
nock(/.*/)
  .get("/api/accounts/users/123/", body => true)
  .reply(200, {
    question_banks: [1, 2, 3]
  });
nock(/.*/)
  .get("/api/auth_code/234", body => true)
  .reply(400, {
    token: "failed"
  });
nock(/.*/)
  .get("/api/auth_code/345", body => true)
  .reply(500, {
    token: "failed"
  });
