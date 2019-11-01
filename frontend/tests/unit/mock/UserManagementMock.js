import nock from "nock";
import UserFactory from "../utils/UserFactory.js";

const user_factory = new UserFactory();

nock(/.*?/)
  .get("/api/accounts/users/")
  .reply(500, {
    result: "Failed"
  });
/*
nock(/.*?/)
    .get(
        "/api/accounts/users/"
    )
    .reply(200, [
        user_factory.create_anonymous_student()
    ])
*/
nock(/.*?/)
  .post("/api/accounts/users/")
  .once()
  .reply(500, {
    result: "Failed"
  });

nock(/.*?/)
  .post("/api/accounts/users/")
  .reply(200, {});

nock(/.*?/)
  .put("/api/accounts/users/500/")
  .reply(500, {
    result: "Failed"
  });

nock(/.*?/)
  .put("/api/accounts/users/200/")
  .reply(200, {});
