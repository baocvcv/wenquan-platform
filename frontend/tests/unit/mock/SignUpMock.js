import nock from "nock";

nock(/.*?/)
  .post("/api/accounts/users/", content => content.username != "fail")
  .reply(200, {
    data: { username: "yes" }
  });
