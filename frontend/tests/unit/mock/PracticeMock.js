import nock from "nock";

nock(/.*/)
  .get("/api/question_banks/0/", body => true)
  .reply(200, {
		questions: []
  });

nock(/.*/)
  .get("/api/question_banks/1/", body => true)
  .reply(200, {
		questions: [1,2,3]
  });

nock(/.*/)
  .get("/api/question_banks/2/", body => true)
  .reply(404, {
	  content: "not found"
  });

nock(/.*/)
  .get("/api/questions/1/", body => true)
  .reply(200, {
	 content: "ok"
  });

nock(/.*/)
  .get("/api/questions/2/", body => true)
  .reply(200, {
	 content: "ok"
  });

nock(/.*/)
  .get("/api/questions/3/", body => true)
  .reply(404, {
	 content: "not found"
  });
