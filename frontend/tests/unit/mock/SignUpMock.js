import nock from "nock";

nock(/.*?/)
	  .post(/.*?/)
	  .reply(200,{
		  data:{username:"yes"}
	  });
