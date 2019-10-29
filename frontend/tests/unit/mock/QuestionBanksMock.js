import nock from "nock";

nock(/.*?/)
  .get("/api/question_banks/")
  .reply(200, () => [ 
    {
      id: 1,
      name: "test",
      brief: "brief",
      picture: "mdi-eye",
      authority: "private",
      createTime: "now",
      lastUpdate: "now",
      question_count: 100,
      invitation_code_count: 0,
      activated_code_count: 0
    }
  ]);
