import nock from "nock";

nock(/.*/)
  .get("/api/papers/0/", body => true)
  .reply(200, {
    is_latest: true
  });

nock(/.*/)
  .get("/api/paper_records?paper=0", body => true)
  .reply(200, [
    {
      is_active: false,
      need_judging: true,
      id: 0
    },
    {
      is_active: true,
      need_juding: false,
      id: 1
    }
  ]);

nock(/.*/)
  .put("/api/paper_records/0", body => true)
  .once()
  .reply(200, [
    {
      is_active: false,
      need_judging: true,
      id: 0
    },
    {
      is_active: true,
      need_juding: false,
      id: 1
    }
  ])
  .put("/api/paper_records/0", body => true)
  .twice()
  .reply(404, "error");
