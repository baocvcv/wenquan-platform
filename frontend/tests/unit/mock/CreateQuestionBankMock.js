import nock from "nock";

nock(/.*?/)
  .post(
    "/api/question_banks/",
    content => content.name != "Error" && content.authority == "public"
  )
  .reply(200, {
    id: 1
  });

nock(/.*?/)
  .post(
    "/api/question_banks/",
    content =>
      content.name != "Error" &&
      content.authority == "private" &&
      !!content.invitation_code_count
  )
  .reply(200, {
    id: 1
  });

nock(/.*?/)
  .post("/api/question_banks/", content => content.name == "Error")
  .reply(404, {
    data: { result: "Error" }
  });
