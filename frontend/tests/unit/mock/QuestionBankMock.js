import nock from "nock";

nock(/.*?/)
  .get("/api/question_banks/200/")
  .reply(200, {
    root_id: 1,
    name: "test_bank",
    picture: "nothinghere",
    brief: "",
    authority: "public",
    createTime: "2019-10-24T16:34:46.293897Z",
    lastUpdate: "2019-10-24T16:34:46.293903Z",
    question_count: 0,
    activated_code_count: 0,
    invitation_code_count: 0,
    questions: [],
    id: 200
  });

nock(/.*?/)
  .get("/api/question_banks/500/")
  .reply(500, {
    result: "Failed"
  });

nock(/.*?/)
  .put("/api/question_banks/200/", body => {
    return body.name === "Fail";
  })
  .reply(500, {
    result: "Fail"
  });

nock(/.*?/)
  .put("/api/question_banks/200/", body => {
    return body.name === "edited";
  })
  .reply(200, {
    result: "Success",
    name: "edited"
  });