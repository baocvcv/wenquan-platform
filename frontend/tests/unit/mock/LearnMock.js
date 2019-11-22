import nock from "nock";

nock(/.*/)
  .post("/api/question_records/", body => true)
  .reply(200, {
	question_id: 0,
  });
