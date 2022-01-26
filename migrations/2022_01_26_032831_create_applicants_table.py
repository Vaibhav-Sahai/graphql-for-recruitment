from orator.migrations import Migration


class CreateApplicantsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('applicants') as table:
            table.increments('id')
            table.timestamp('timestamp')
            table.text('email')
            table.string('name')
            table.string('year')
            table.string('major')
            table.string('second_major')
            table.string('minor')
            table.string('second_minor')
            table.string('gpa')
            table.string('website')
            table.enum('division', ['Software Development', 'Strategy Implementation', 'Quanitative Research', 'External Affairs'])
            table.text('why_team')
            table.string('commitment')
            table.text('value_to_club')
            table.text('personal_goals')
            table.string('assessment')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('applicants')
