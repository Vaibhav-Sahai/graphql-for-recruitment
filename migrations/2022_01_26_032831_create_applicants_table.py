from orator.migrations import Migration


class CreateApplicantsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('applicants') as table:
            table.increments('id')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('applicants')
