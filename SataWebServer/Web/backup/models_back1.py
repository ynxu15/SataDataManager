# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TempExpertPatent(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    expert_id = models.TextField(db_column='EXPERT_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    protection_time = models.TextField(db_column='PROTECTION_TIME', blank=True, null=True)  # Field name made lowercase.
    patent_name = models.TextField(db_column='PATENT_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    authorized_state = models.TextField(db_column='AUTHORIZED_STATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    patent_domain = models.TextField(db_column='PATENT_DOMAIN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    patentee_seq = models.TextField(db_column='PATENTEE_SEQ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    patent_type = models.TextField(db_column='PATENT_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    register_date = models.TextField(db_column='REGISTER_DATE', blank=True, null=True)  # Field name made lowercase.
    application = models.TextField(db_column='APPLICATION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ordernum = models.TextField(db_column='ORDERNUM')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_temp_expert_patent'


class TempExpertProjectInfo(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    expert_id = models.TextField(db_column='EXPERT_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    start_time = models.TextField(db_column='START_TIME', blank=True, null=True)  # Field name made lowercase.
    end_time = models.TextField(db_column='END_TIME', blank=True, null=True)  # Field name made lowercase.
    project_name = models.TextField(db_column='PROJECT_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fundsource = models.TextField(db_column='FUNDSOURCE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expenditure = models.TextField(db_column='EXPENDITURE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    effect = models.TextField(db_column='EFFECT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ordernum = models.TextField(db_column='ORDERNUM')  # Field name made lowercase. This field type is a guess.
    statk_holder = models.TextField(db_column='STATK_HOLDER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_temp_expert_project_info'


class TempExpertRepresentPapers(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    expert_id = models.TextField(db_column='EXPERT_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    publish_time = models.TextField(db_column='PUBLISH_TIME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    title = models.TextField(db_column='TITLE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    author_order = models.TextField(db_column='AUTHOR_ORDER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    thesis_domain = models.TextField(db_column='THESIS_DOMAIN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    publish_house = models.TextField(db_column='PUBLISH_HOUSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    publication_level = models.TextField(db_column='PUBLICATION_LEVEL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    influence = models.TextField(db_column='INFLUENCE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ordernum = models.TextField(db_column='ORDERNUM')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_temp_expert_represent_papers'


class TempProTcRegisterUser(models.Model):
    user_id = models.TextField(db_column='USER_ID')  # Field name made lowercase. This field type is a guess.
    register_id = models.TextField(db_column='REGISTER_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    relat_type = models.TextField(db_column='RELAT_TYPE')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_temp_pro_tc_register_user'


#class A1(models.Model):
#    id = models.TextField(blank=True, null=True, primary_key=True)  # This field type is a guess.
#    name = models.TextField(blank=True, null=True)  # This field type is a guess.
#
#    class Meta:
#        managed = False
#        db_table = 'a1'
#
#
#class A2(models.Model):
#    id = models.TextField(blank=True, null=True, primary_key=True)  # This field type is a guess.
#    name = models.TextField(blank=True, null=True)  # This field type is a guess.
#
#    class Meta:
#        managed = False
#        db_table = 'a2'
#
#
#class A3(models.Model):
#    id = models.TextField(blank=True, null=True, primary_key=True)  # This field type is a guess.
#    name = models.TextField(blank=True, null=True)  # This field type is a guess.
#
#    class Meta:
#        managed = False
#        db_table = 'a3'


class A4(models.Model):
    code = models.TextField(blank=True, null=True)  # This field type is a guess.
    name = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'a4'


class AchievementChangeInfoTemp(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    change_ago_company_name = models.TextField(db_column='CHANGE_AGO_COMPANY_NAME')  # Field name made lowercase. This field type is a guess.
    change_later_company_name = models.TextField(db_column='CHANGE_LATER_COMPANY_NAME')  # Field name made lowercase. This field type is a guess.
    org_code = models.TextField(db_column='ORG_CODE')  # Field name made lowercase. This field type is a guess.
    document_no = models.TextField(db_column='DOCUMENT_NO')  # Field name made lowercase. This field type is a guess.
    project_name = models.TextField(db_column='PROJECT_NAME')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'achievement_change_info_temp'


class AchievementPatentInfoTemp(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    project_name = models.TextField(db_column='PROJECT_NAME')  # Field name made lowercase. This field type is a guess.
    document_no = models.TextField(db_column='DOCUMENT_NO')  # Field name made lowercase. This field type is a guess.
    company_name = models.TextField(db_column='COMPANY_NAME')  # Field name made lowercase. This field type is a guess.
    org_code = models.TextField(db_column='ORG_CODE')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'achievement_patent_info_temp'


class AchievementProjectInfoTemp(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    document_no = models.TextField(db_column='DOCUMENT_NO')  # Field name made lowercase. This field type is a guess.
    project_name = models.TextField(db_column='PROJECT_NAME')  # Field name made lowercase. This field type is a guess.
    year = models.TextField(db_column='YEAR')  # Field name made lowercase. This field type is a guess.
    company_name = models.TextField(db_column='COMPANY_NAME')  # Field name made lowercase. This field type is a guess.
    org_code = models.TextField(db_column='ORG_CODE')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'achievement_project_info_temp'


class AnimalSelection(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    org_name = models.TextField(db_column='ORG_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    grant_license = models.TextField(db_column='GRANT_LICENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    grant_org = models.TextField(db_column='GRANT_ORG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    valid_from = models.TextField(db_column='VALID_FROM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    valid_to = models.TextField(db_column='VALID_TO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    license_status = models.TextField(db_column='LICENSE_STATUS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    grant_date = models.TextField(db_column='GRANT_DATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    details = models.TextField(db_column='DETAILS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    org_address = models.TextField(db_column='ORG_ADDRESS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_name = models.TextField(db_column='F_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_contact = models.TextField(db_column='F_CONTACT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    type = models.TextField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    l_name = models.TextField(db_column='L_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    l_contact = models.TextField(db_column='L_CONTACT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    real_address = models.TextField(db_column='REAL_ADDRESS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_type = models.TextField(db_column='SELECTION_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_date = models.TextField(db_column='SELECTION_DATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_content = models.TextField(db_column='SELECTION_CONTENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_issue = models.TextField(db_column='SELECTION_ISSUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_result = models.TextField(db_column='SELECTION_RESULT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_criteria = models.TextField(db_column='SELECTION_CRITERIA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_dept = models.TextField(db_column='SELECTION_DEPT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_person = models.TextField(db_column='SELECTION_PERSON', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    is_select = models.TextField(db_column='IS_SELECT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    is_chosen = models.TextField(db_column='IS_CHOSEN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'animal_selection'


class AnimalSelectionResult(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    org_name = models.TextField(db_column='ORG_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    grant_license = models.TextField(db_column='GRANT_LICENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    grant_org = models.TextField(db_column='GRANT_ORG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    valid_from = models.TextField(db_column='VALID_FROM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    valid_to = models.TextField(db_column='VALID_TO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    license_status = models.TextField(db_column='LICENSE_STATUS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    grant_date = models.TextField(db_column='GRANT_DATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    details = models.TextField(db_column='DETAILS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    org_address = models.TextField(db_column='ORG_ADDRESS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_name = models.TextField(db_column='F_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_contact = models.TextField(db_column='F_CONTACT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    type = models.TextField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    l_name = models.TextField(db_column='L_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    l_contact = models.TextField(db_column='L_CONTACT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    real_address = models.TextField(db_column='REAL_ADDRESS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_type = models.TextField(db_column='SELECTION_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_date = models.TextField(db_column='SELECTION_DATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_content = models.TextField(db_column='SELECTION_CONTENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_issue = models.TextField(db_column='SELECTION_ISSUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_result = models.TextField(db_column='SELECTION_RESULT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_criteria = models.TextField(db_column='SELECTION_CRITERIA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_dept = models.TextField(db_column='SELECTION_DEPT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_person = models.TextField(db_column='SELECTION_PERSON', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    is_select = models.TextField(db_column='IS_SELECT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_reason = models.TextField(db_column='SELECTION_REASON', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_category = models.TextField(db_column='SELECTION_CATEGORY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_project = models.TextField(db_column='SELECTION_PROJECT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    deal_person = models.TextField(db_column='DEAL_PERSON', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    deal_org = models.TextField(db_column='DEAL_ORG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    is_gaozhi = models.TextField(db_column='IS_GAOZHI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    gaozhi_date = models.TextField(db_column='GAOZHI_DATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    gaozhi_method = models.TextField(db_column='GAOZHI_METHOD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_place = models.TextField(db_column='SELECTION_PLACE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_list = models.TextField(db_column='SELECTION_LIST', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    check_date = models.TextField(db_column='CHECK_DATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    check_person = models.TextField(db_column='CHECK_PERSON', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    check_opinion = models.TextField(db_column='CHECK_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    check_method = models.TextField(db_column='CHECK_METHOD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    shenhe_person = models.TextField(db_column='SHENHE_PERSON', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    shenhe_date = models.TextField(db_column='SHENHE_DATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    shenhe_opinion = models.TextField(db_column='SHENHE_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    jueding_person = models.TextField(db_column='JUEDING_PERSON', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    jueding_date = models.TextField(db_column='JUEDING_DATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    jueding_opinion = models.TextField(db_column='JUEDING_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_conclusion = models.TextField(db_column='SELECTION_CONCLUSION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fail_reason = models.TextField(db_column='FAIL_REASON', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hege_chuli = models.TextField(db_column='HEGE_CHULI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buhege_leibie = models.TextField(db_column='BUHEGE_LEIBIE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buhege_neirong = models.TextField(db_column='BUHEGE_NEIRONG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buhege_chengxu = models.TextField(db_column='BUHEGE_CHENGXU', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'animal_selection_result'


class AnimalSelectionTemp(models.Model):
    org_name = models.TextField(db_column='ORG_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    grant_license = models.TextField(db_column='GRANT_LICENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    grant_org = models.TextField(db_column='GRANT_ORG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    valid_from = models.TextField(db_column='VALID_FROM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    valid_to = models.TextField(db_column='VALID_TO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    license_status = models.TextField(db_column='LICENSE_STATUS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    grant_date = models.TextField(db_column='GRANT_DATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    details = models.TextField(db_column='DETAILS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    org_address = models.TextField(db_column='ORG_ADDRESS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_name = models.TextField(db_column='F_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_contact = models.TextField(db_column='F_CONTACT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    type = models.TextField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    l_name = models.TextField(db_column='L_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    l_contact = models.TextField(db_column='L_CONTACT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    real_address = models.TextField(db_column='REAL_ADDRESS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_type = models.TextField(db_column='SELECTION_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_date = models.TextField(db_column='SELECTION_DATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_content = models.TextField(db_column='SELECTION_CONTENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_issue = models.TextField(db_column='SELECTION_ISSUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_result = models.TextField(db_column='SELECTION_RESULT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_criteria = models.TextField(db_column='SELECTION_CRITERIA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selection_dept = models.TextField(db_column='SELECTION_DEPT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    is_select = models.TextField(db_column='IS_SELECT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    is_chosen = models.TextField(db_column='IS_CHOSEN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'animal_selection_temp'


class ApplyAcceptView(models.Model):
    applyno = models.TextField(db_column='APPLYNO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    result = models.TextField(db_column='RESULT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    suggestion = models.TextField(db_column='SUGGESTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    opdepartcode = models.TextField(db_column='OPDEPARTCODE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    opdepartname = models.TextField(db_column='OPDEPARTNAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    opuserid = models.TextField(db_column='OPUSERID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    opusername = models.TextField(db_column='OPUSERNAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    optime = models.TextField(db_column='OPTIME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    latestupdatetime = models.TextField(db_column='LATESTUPDATETIME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'apply_accept_view'


class ApplyCollectView(models.Model):
    applyno = models.TextField(db_column='APPLYNO', unique=True)  # Field name made lowercase. This field type is a guess.
    suggestion = models.TextField(db_column='SUGGESTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    opdepartcode = models.TextField(db_column='OPDEPARTCODE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    opdepartname = models.TextField(db_column='OPDEPARTNAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    opuserid = models.TextField(db_column='OPUSERID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    opusername = models.TextField(db_column='OPUSERNAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    optime = models.TextField(db_column='OPTIME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    latestupdatetime = models.TextField(db_column='LATESTUPDATETIME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'apply_collect_view'


class ApplyCorrectView(models.Model):
    applyno = models.TextField(db_column='APPLYNO', unique=True)  # Field name made lowercase. This field type is a guess.
    suggestion = models.TextField(db_column='SUGGESTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    opdepartcode = models.TextField(db_column='OPDEPARTCODE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    opdepartname = models.TextField(db_column='OPDEPARTNAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    opuserid = models.TextField(db_column='OPUSERID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    opusername = models.TextField(db_column='OPUSERNAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    optime = models.TextField(db_column='OPTIME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stuffid = models.TextField(db_column='STUFFID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stuffsuggestion = models.TextField(db_column='STUFFSUGGESTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    latestupdatetime = models.TextField(db_column='LATESTUPDATETIME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'apply_correct_view'


class ApplyPassView(models.Model):
    applyno = models.TextField(db_column='APPLYNO', unique=True)  # Field name made lowercase. This field type is a guess.
    suggestion = models.TextField(db_column='SUGGESTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    opdepartcode = models.TextField(db_column='OPDEPARTCODE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    opdepartname = models.TextField(db_column='OPDEPARTNAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    opuserid = models.TextField(db_column='OPUSERID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    opusername = models.TextField(db_column='OPUSERNAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    optime = models.TextField(db_column='OPTIME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    latestupdatetime = models.TextField(db_column='LATESTUPDATETIME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'apply_pass_view'


class ApplySaveView(models.Model):
    applyno = models.TextField(db_column='APPLYNO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    itemcode = models.TextField(db_column='ITEMCODE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    itemname = models.TextField(db_column='ITEMNAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    targettype = models.TextField(db_column='TARGETTYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    targetname = models.TextField(db_column='TARGETNAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    targetno = models.TextField(db_column='TARGETNO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    userid = models.TextField(db_column='USERID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    username = models.TextField(db_column='USERNAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    licensetype = models.TextField(db_column='LICENSETYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    licenseno = models.TextField(db_column='LICENSENO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mobile = models.TextField(db_column='MOBILE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    content = models.TextField(db_column='CONTENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    optime = models.TextField(db_column='OPTIME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    latestupdatetime = models.TextField(db_column='LATESTUPDATETIME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'apply_save_view'


class ApplySubmitView(models.Model):
    applyno = models.TextField(db_column='APPLYNO', unique=True)  # Field name made lowercase. This field type is a guess.
    optime = models.TextField(db_column='OPTIME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    latestupdatetime = models.TextField(db_column='LATESTUPDATETIME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'apply_submit_view'


class Buyerinfo(models.Model):
    buyerno = models.TextField(unique=True)  # This field type is a guess.
    buyername = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyertype = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyertype_view = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyersite = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyercountrygxqqy = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyercountrytype = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyercountrytype_view = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyerregisterdate = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyeruserloginname = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyerusername = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyersite_view = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyerzipcode = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyeraddress = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyerrepresentative = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyerretelephone = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyerreemail = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyercontact = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyercontacttel = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyercontactemail = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyerjsjdm = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyerswdjzh = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyerzzjgdmzh = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyersfzh = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyerhzzh = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyerparkname = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyergmjjhy = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyergmjjhy_view = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyerscale = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyerscale_view = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyerisyfjg = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyerkjfwjg = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyerkjfwjg_view = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyerkjfwjgmc = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyerjszyjg = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyerjszyjg_view = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyerjszyjgmc = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyerislist = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyersecuritycode = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyer_zzkyys = models.TextField(blank=True, null=True)  # This field type is a guess.
    measureinfo = models.TextField(blank=True, null=True)  # This field type is a guess.
    uploadflag = models.TextField(blank=True, null=True)  # This field type is a guess.
    firsttime = models.TextField(blank=True, null=True)  # This field type is a guess.
    latestinfo = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'buyerinfo'


class Buyerinforcv(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    buyerno = models.TextField(db_column='BuyerNo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyername = models.TextField(db_column='BuyerName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyercountrytype = models.TextField(db_column='BuyerCountryType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyercountrytype_view = models.TextField(db_column='BuyerCountryType_View', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyerregisterdate = models.TextField(db_column='BuyerRegisterDate', blank=True, null=True)  # Field name made lowercase.
    buyeruserloginname = models.TextField(db_column='BuyerUserLoginName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyerusername = models.TextField(db_column='BuyerUserName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyersite = models.TextField(db_column='BuyerSite', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyersite_view = models.TextField(db_column='BuyerSite_View', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyerzipcode = models.TextField(db_column='BuyerZipCode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyeraddress = models.TextField(db_column='BuyerAddress', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyerrepresentative = models.TextField(db_column='BuyerRepresentative', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyerretelephone = models.TextField(db_column='BuyerRetelephone', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyercontact = models.TextField(db_column='BuyerContact', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyercontacttel = models.TextField(db_column='BuyerContactTel', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyercontactemail = models.TextField(db_column='BuyerContactEmail', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyertype = models.TextField(db_column='BuyerType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyertype_view = models.TextField(db_column='BuyerType_View', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyerjsjdm = models.TextField(db_column='BuyerJsjdm', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyerswdjzh = models.TextField(db_column='BuyerSwdjzh', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyerzzjgdmzh = models.TextField(db_column='BuyerZzjgdmzh', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyersfzh = models.TextField(db_column='BuyerSfzh', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyerhzzh = models.TextField(db_column='BuyerHzzh', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyercountrygxqqy = models.TextField(db_column='BuyerCountryGxqqy', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyerparkname = models.TextField(db_column='BuyerParkName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyergmjjhy = models.TextField(db_column='BuyerGmjjhy', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyergmjjhy_view = models.TextField(db_column='BuyerGmjjhy_View', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyerscale = models.TextField(db_column='BuyerScale', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyerscale_view = models.TextField(db_column='BuyerScale_View', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyerisyfjg = models.TextField(db_column='BuyerIsyfjg', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyerjszyjg = models.TextField(db_column='BuyerJszyjg', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyerjszyjg_view = models.TextField(db_column='BuyerJszyjg_View', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyerjszyjgmc = models.TextField(db_column='BuyerJszyjgmc', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyerislist = models.TextField(db_column='BuyerIslist', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyersecuritycode = models.TextField(db_column='BuyerSecurityCode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyer_zzkyys = models.TextField(db_column='Buyer_Zzkyys', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyerkjfwjg = models.TextField(db_column='BuyerKjfwjg', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyerkjfwjg_view = models.TextField(db_column='BuyerKjfwjg_view', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buyerkjfwjgmc = models.TextField(db_column='BuyerKjfwjgmc', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    measureinfo = models.TextField(db_column='MeasureInfo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    downloadflag = models.TextField(db_column='DownloadFlag', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    firsttime = models.TextField(db_column='FirstTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'buyerinforcv'


class CompanyBaseInfoTemp(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    company_name = models.TextField(db_column='COMPANY_NAME')  # Field name made lowercase. This field type is a guess.
    org_code = models.TextField(db_column='ORG_CODE')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'company_base_info_temp'


class Comparedtemp(models.Model):
    id = models.TextField(unique=True, primary_key=True)  # This field type is a guess.
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    number = models.TextField(blank=True, null=True)  # This field type is a guess.
    senddate = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'comparedtemp'


class Contractbuyer(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    contractid = models.TextField(blank=True, null=True)  # This field type is a guess.
    sellerno = models.TextField(blank=True, null=True)  # This field type is a guess.
    buyerno = models.TextField(blank=True, null=True)  # This field type is a guess.
    measureinfo = models.TextField(blank=True, null=True)  # This field type is a guess.
    firsttime = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'contractbuyer'


class Contractbuyerrcv(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    contractid = models.TextField(db_column='CONTRACTID')  # Field name made lowercase. This field type is a guess.
    sellerno = models.TextField(db_column='SELLERNO')  # Field name made lowercase. This field type is a guess.
    buyerno = models.TextField(db_column='BUYERNO')  # Field name made lowercase. This field type is a guess.
    measureinfo = models.TextField(db_column='MeasureInfo')  # Field name made lowercase. This field type is a guess.
    downloadflag = models.TextField(db_column='DownloadFlag')  # Field name made lowercase. This field type is a guess.
    firsttime = models.TextField(db_column='FirstTime', blank=True, null=True)  # Field name made lowercase.
    transno = models.TextField(db_column='TransNo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'contractbuyerrcv'


class Contractregisterinfo(models.Model):
    id = models.TextField(unique=True, primary_key=True)  # This field type is a guess.
    contractno = models.TextField(blank=True, null=True)  # This field type is a guess.
    projectname = models.TextField(db_column='ProjectName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isseller = models.TextField(db_column='IsSeller')  # Field name made lowercase. This field type is a guess.
    conuserloginname = models.TextField(blank=True, null=True)  # This field type is a guess.
    conusername = models.TextField(blank=True, null=True)  # This field type is a guess.
    deptno = models.TextField(db_column='DeptNo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    declaredate = models.TextField(blank=True, null=True)  # This field type is a guess.
    conregisterdate = models.TextField(blank=True, null=True)  # This field type is a guess.
    totalamount = models.TextField(blank=True, null=True)  # This field type is a guess.
    technicalamount = models.TextField(blank=True, null=True)  # This field type is a guess.
    signdate = models.TextField(blank=True, null=True)  # This field type is a guess.
    contractbegindate = models.TextField(blank=True, null=True)  # This field type is a guess.
    contractenddate = models.TextField(blank=True, null=True)  # This field type is a guess.
    contracttype = models.TextField(blank=True, null=True)  # This field type is a guess.
    contracttype_view = models.TextField(blank=True, null=True)  # This field type is a guess.
    paymethod = models.TextField(blank=True, null=True)  # This field type is a guess.
    paymethod_view = models.TextField(blank=True, null=True)  # This field type is a guess.
    projectplantype = models.TextField(blank=True, null=True)  # This field type is a guess.
    projectplantype_view = models.TextField(blank=True, null=True)  # This field type is a guess.
    ipr = models.TextField(blank=True, null=True)  # This field type is a guess.
    ipr_view = models.TextField(blank=True, null=True)  # This field type is a guess.
    patentnum = models.TextField(blank=True, null=True)  # This field type is a guess.
    in_patentnum = models.TextField(blank=True, null=True)  # This field type is a guess.
    um_patentnum = models.TextField(blank=True, null=True)  # This field type is a guess.
    ad_patentnum = models.TextField(blank=True, null=True)  # This field type is a guess.
    techarea = models.TextField(blank=True, null=True)  # This field type is a guess.
    techarea_view = models.TextField(blank=True, null=True)  # This field type is a guess.
    economicobj = models.TextField(blank=True, null=True)  # This field type is a guess.
    economicobj_view = models.TextField(blank=True, null=True)  # This field type is a guess.
    serviceindus = models.TextField(blank=True, null=True)  # This field type is a guess.
    serviceindus_view = models.TextField(blank=True, null=True)  # This field type is a guess.
    topicname = models.TextField(blank=True, null=True)  # This field type is a guess.
    topicno = models.TextField(blank=True, null=True)  # This field type is a guess.
    authorizedno = models.TextField(blank=True, null=True)  # This field type is a guess.
    isrelated = models.TextField(blank=True, null=True)  # This field type is a guess.
    contractstatusid = models.TextField(blank=True, null=True)  # This field type is a guess.
    receivedate = models.TextField(blank=True, null=True)  # This field type is a guess.
    approvedate = models.TextField(blank=True, null=True)  # This field type is a guess.
    measureinfo = models.TextField(blank=True, null=True)  # This field type is a guess.
    uploadflag = models.TextField(blank=True, null=True)  # This field type is a guess.
    firsttime = models.TextField(blank=True, null=True)  # This field type is a guess.
    uploadinfo = models.TextField(blank=True, null=True)  # This field type is a guess.
    serialnum = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'contractregisterinfo'


class Contractregisterinforcv(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    projectname = models.TextField(db_column='ProjectName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isseller = models.TextField(db_column='IsSeller', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    deptno = models.TextField(db_column='DeptNo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    declaredate = models.TextField(db_column='DeclareDate', blank=True, null=True)  # Field name made lowercase.
    conregisterdate = models.TextField(db_column='ConRegisterDate', blank=True, null=True)  # Field name made lowercase.
    conuserloginname = models.TextField(db_column='ConUserLoginName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conusername = models.TextField(db_column='ConUserName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    totalamount = models.TextField(db_column='TotalAmount', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    technicalamount = models.TextField(db_column='TechnicalAmount', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    signdate = models.TextField(db_column='SignDate', blank=True, null=True)  # Field name made lowercase.
    contractbegindate = models.TextField(db_column='ContractBeginDate', blank=True, null=True)  # Field name made lowercase.
    contractenddate = models.TextField(db_column='ContractEndDate', blank=True, null=True)  # Field name made lowercase.
    paymethod = models.TextField(db_column='PayMethod', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    paymethod_view = models.TextField(db_column='PayMethod_View', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    contracttype = models.TextField(db_column='ContractType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    contracttype_view = models.TextField(db_column='ContractType_View', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ipr = models.TextField(db_column='Ipr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ipr_view = models.TextField(db_column='Ipr_View', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    patentnum = models.TextField(db_column='PatentNum', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    in_patentnum = models.TextField(db_column='In_PatentNum', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    um_patentnum = models.TextField(db_column='Um_PatentNum', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ad_patentnum = models.TextField(db_column='Ad_PatentNum', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    techarea = models.TextField(db_column='TechArea', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    techarea_view = models.TextField(db_column='TechArea_VIEW', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    projectplantype = models.TextField(db_column='ProjectPlanType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    projectplantype_view = models.TextField(db_column='ProjectPlanType_View', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    economicobj = models.TextField(db_column='EconomicObj', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    economicobj_view = models.TextField(db_column='EconomicObj_View', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    serviceindus = models.TextField(db_column='ServiceIndus', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    serviceindus_view = models.TextField(db_column='ServiceIndus_View', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isrelated = models.TextField(db_column='IsRelated', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    topicname = models.TextField(db_column='TopicName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    topicno = models.TextField(db_column='TopicNo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    authorizedno = models.TextField(db_column='AuthorizedNo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    contractstatusid = models.TextField(db_column='ContractStatusId', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    receivedate = models.TextField(db_column='ReceiveDate', blank=True, null=True)  # Field name made lowercase.
    approvedate = models.TextField(db_column='ApproveDate', blank=True, null=True)  # Field name made lowercase.
    measureinfo = models.TextField(db_column='MeasureInfo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    downloadflag = models.TextField(db_column='DownloadFlag', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    firsttime = models.TextField(db_column='FirstTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contractregisterinforcv'


class DataImportAchievementsChangeInfo(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    change_ago_company_name = models.TextField(db_column='CHANGE_AGO_COMPANY_NAME')  # Field name made lowercase. This field type is a guess.
    change_later_company_name = models.TextField(db_column='CHANGE_LATER_COMPANY_NAME')  # Field name made lowercase. This field type is a guess.
    org_code = models.TextField(db_column='ORG_CODE')  # Field name made lowercase. This field type is a guess.
    project_id = models.TextField(db_column='PROJECT_ID')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_import_achievements_change_info'


class DataImportAchievementsProjectInfo(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    project_id = models.TextField(db_column='PROJECT_ID')  # Field name made lowercase. This field type is a guess.
    project_number = models.TextField(db_column='PROJECT_NUMBER')  # Field name made lowercase. This field type is a guess.
    project_name = models.TextField(db_column='PROJECT_NAME')  # Field name made lowercase. This field type is a guess.
    company_id = models.TextField(db_column='COMPANY_ID')  # Field name made lowercase. This field type is a guess.
    have_imported = models.TextField(db_column='HAVE_IMPORTED', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_import_achievements_project_info'


class DataImportAchievementsPropertyInfo(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    project_id = models.TextField(db_column='PROJECT_ID')  # Field name made lowercase. This field type is a guess.
    intellectual_name = models.TextField(db_column='INTELLECTUAL_NAME')  # Field name made lowercase. This field type is a guess.
    intellectual_type = models.TextField(db_column='INTELLECTUAL_TYPE')  # Field name made lowercase. This field type is a guess.
    palent_number = models.TextField(db_column='PALENT_NUMBER')  # Field name made lowercase. This field type is a guess.
    is_investigation_stage = models.TextField(db_column='IS_INVESTIGATION_STAGE')  # Field name made lowercase. This field type is a guess.
    grant_date = models.TextField(db_column='GRANT_DATE', blank=True, null=True)  # Field name made lowercase.
    apply_date = models.TextField(db_column='APPLY_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_import_achievements_property_info'


class DataImportBookmaking(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    id_expert_bookmaking = models.TextField(db_column='ID_EXPERT_BOOKMAKING')  # Field name made lowercase. This field type is a guess.
    thesis_name = models.TextField(db_column='THESIS_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    thesis_domain = models.TextField(db_column='THESIS_DOMAIN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    author_seq = models.TextField(db_column='AUTHOR_SEQ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    publishhouse = models.TextField(db_column='PUBLISHHOUSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    vol_number = models.TextField(db_column='VOL_NUMBER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    publicationlevel = models.TextField(db_column='PUBLICATIONLEVEL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    id_expert_base = models.TextField(db_column='ID_EXPERT_BASE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ordernum = models.TextField(db_column='ORDERNUM')  # Field name made lowercase. This field type is a guess.
    influence = models.TextField(db_column='INFLUENCE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_import_bookmaking'


class DataImportCompanyInfo(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    company_id = models.TextField(db_column='COMPANY_ID')  # Field name made lowercase. This field type is a guess.
    company_name = models.TextField(db_column='COMPANY_NAME')  # Field name made lowercase. This field type is a guess.
    org_code = models.TextField(db_column='ORG_CODE')  # Field name made lowercase. This field type is a guess.
    have_imported = models.TextField(db_column='HAVE_IMPORTED', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_import_company_info'


class DataImportCompanyInfoBak(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    company_id = models.TextField(db_column='COMPANY_ID')  # Field name made lowercase. This field type is a guess.
    company_name = models.TextField(db_column='COMPANY_NAME')  # Field name made lowercase. This field type is a guess.
    org_code = models.TextField(db_column='ORG_CODE')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_import_company_info_bak'


class DataImportCompanyInfoChange(models.Model):
    old_company_name = models.TextField(db_column='OLD_COMPANY_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    new_company_name = models.TextField(db_column='NEW_COMPANY_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    org_code = models.TextField(db_column='ORG_CODE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_import_company_info_change'


class DataImportExpertAccount(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    account_id = models.TextField(db_column='ACCOUNT_ID')  # Field name made lowercase. This field type is a guess.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createdate = models.TextField(db_column='CREATEDATE', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    pass_field = models.TextField(db_column='PASS', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word. This field type is a guess.
    valid = models.TextField(db_column='VALID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    removed = models.TextField(db_column='REMOVED', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lastchg = models.TextField(db_column='LASTCHG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    imin = models.TextField(db_column='IMIN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    imax = models.TextField(db_column='IMAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    warn = models.TextField(db_column='WARN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    inact = models.TextField(db_column='INACT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expire = models.TextField(db_column='EXPIRE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    personnel = models.TextField(db_column='PERSONNEL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    personeltype = models.TextField(db_column='PERSONELTYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    startdate = models.TextField(db_column='STARTDATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_import_expert_account'


class DataImportExpertAchievement(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    id_expert_achievement = models.TextField(db_column='ID_EXPERT_ACHIEVEMENT')  # Field name made lowercase. This field type is a guess.
    project_name = models.TextField(db_column='PROJECT_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    workdomain = models.TextField(db_column='WORKDOMAIN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    effect = models.TextField(db_column='EFFECT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    unit = models.TextField(db_column='UNIT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    finish_time = models.TextField(db_column='FINISH_TIME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    achievement_level = models.TextField(db_column='ACHIEVEMENT_LEVEL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    id_expert_base = models.TextField(db_column='ID_EXPERT_BASE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ordernum = models.TextField(db_column='ORDERNUM')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_import_expert_achievement'


class DataImportExpertAttendIndividualInfo(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    id_expert_attend_individual = models.TextField(db_column='ID_EXPERT_ATTEND_INDIVIDUAL')  # Field name made lowercase. This field type is a guess.
    id_expert_base = models.TextField(db_column='ID_EXPERT_BASE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    individual_year = models.TextField(db_column='INDIVIDUAL_YEAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    attend_pro_num = models.TextField(db_column='ATTEND_PRO_NUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    individual_pro_num = models.TextField(db_column='INDIVIDUAL_PRO_NUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createdate = models.TextField(db_column='CREATEDATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_import_expert_attend_individual_info'


class DataImportExpertAuditLog(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    id_expert_audit_log = models.TextField(db_column='ID_EXPERT_AUDIT_LOG')  # Field name made lowercase. This field type is a guess.
    id_expert_base = models.TextField(db_column='ID_EXPERT_BASE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    auditperson = models.TextField(db_column='AUDITPERSON', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    audittime = models.TextField(db_column='AUDITTIME', blank=True, null=True)  # Field name made lowercase.
    papermaterial = models.TextField(db_column='PAPERMATERIAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    remark = models.TextField(db_column='REMARK', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_import_expert_audit_log'


class DataImportExpertBaseInfo(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    id_expert_base = models.TextField(db_column='ID_EXPERT_BASE')  # Field name made lowercase. This field type is a guess.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    photo = models.TextField(db_column='PHOTO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    gender = models.TextField(db_column='GENDER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    birth_date = models.TextField(db_column='BIRTH_DATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    id_number = models.TextField(db_column='ID_NUMBER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    id_type = models.TextField(db_column='ID_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mobile_phone = models.TextField(db_column='MOBILE_PHONE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mailbox = models.TextField(db_column='MAILBOX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    home_address = models.TextField(db_column='HOME_ADDRESS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    home_zip = models.TextField(db_column='HOME_ZIP', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    home_phone = models.TextField(db_column='HOME_PHONE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    culture_level = models.TextField(db_column='CULTURE_LEVEL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    foreign_lang_type = models.TextField(db_column='FOREIGN_LANG_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    foreign_lang_level = models.TextField(db_column='FOREIGN_LANG_LEVEL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    foreign_lang_type2 = models.TextField(db_column='FOREIGN_LANG_TYPE2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    foreign_lang_level2 = models.TextField(db_column='FOREIGN_LANG_LEVEL2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    degree_level = models.TextField(db_column='DEGREE_LEVEL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    degree_country = models.TextField(db_column='DEGREE_COUNTRY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    unit_name = models.TextField(db_column='UNIT_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    unitzip = models.TextField(db_column='UNITZIP', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    unit_address = models.TextField(db_column='UNIT_ADDRESS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fax = models.TextField(db_column='FAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    department = models.TextField(db_column='DEPARTMENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    unit_phone1 = models.TextField(db_column='UNIT_PHONE1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    unit_phone2 = models.TextField(db_column='UNIT_PHONE2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    position = models.TextField(db_column='POSITION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    title = models.TextField(db_column='TITLE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    major = models.TextField(db_column='MAJOR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    work_domain = models.TextField(db_column='WORK_DOMAIN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    other_major = models.TextField(db_column='OTHER_MAJOR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expert_check_state = models.TextField(db_column='EXPERT_CHECK_STATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    memo = models.TextField(db_column='MEMO', blank=True, null=True)  # Field name made lowercase.
    mailbox2 = models.TextField(db_column='MAILBOX2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mailbox3 = models.TextField(db_column='MAILBOX3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherunit1 = models.TextField(db_column='OTHERUNIT1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherunit2 = models.TextField(db_column='OTHERUNIT2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherunit3 = models.TextField(db_column='OTHERUNIT3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otherdomain = models.TextField(db_column='OTHERDOMAIN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    vocation = models.TextField(db_column='VOCATION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    specialtytype = models.TextField(db_column='SPECIALTYTYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    workingdomain = models.TextField(db_column='WORKINGDOMAIN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    creditlevel = models.TextField(db_column='CREDITLEVEL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    specialty = models.TextField(db_column='SPECIALTY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    specialtydescription = models.TextField(db_column='SPECIALTYDESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    distribution = models.TextField(db_column='DISTRIBUTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    importproject = models.TextField(db_column='IMPORTPROJECT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expertlastupdatetime = models.TextField(db_column='EXPERTLASTUPDATETIME', blank=True, null=True)  # Field name made lowercase.
    politytitle = models.TextField(db_column='POLITYTITLE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expertsubject = models.TextField(db_column='EXPERTSUBJECT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expertsubjectname = models.TextField(db_column='EXPERTSUBJECTNAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    workingdomainname = models.TextField(db_column='WORKINGDOMAINNAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    vocationname = models.TextField(db_column='VOCATIONNAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    zrjjcode = models.TextField(db_column='ZRJJCODE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    zrjjcodename = models.TextField(db_column='ZRJJCODENAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isinsh = models.TextField(db_column='ISINSH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    domainkeyword = models.TextField(db_column='DOMAINKEYWORD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    banktype = models.TextField(db_column='BANKTYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bankaddress = models.TextField(db_column='BANKADDRESS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bankbranch = models.TextField(db_column='BANKBRANCH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    banknumber = models.TextField(db_column='BANKNUMBER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_import_expert_base_info'


class DataImportExpertBaseLog(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    id_expert_base_log = models.TextField(db_column='ID_EXPERT_BASE_LOG')  # Field name made lowercase. This field type is a guess.
    id_expert_base = models.TextField(db_column='ID_EXPERT_BASE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    updatemanager = models.TextField(db_column='UPDATEMANAGER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    info = models.TextField(db_column='INFO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    date_in = models.TextField(db_column='DATE_IN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_import_expert_base_log'


class DataImportExpertCheckList(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    id_expertcheck_list = models.TextField(db_column='ID_EXPERTCHECK_LIST')  # Field name made lowercase. This field type is a guess.
    source = models.TextField(db_column='SOURCE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    projectgroupid = models.TextField(db_column='PROJECTGROUPID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    projectgroupname = models.TextField(db_column='PROJECTGROUPNAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    projectnum = models.TextField(db_column='PROJECTNUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cscode = models.TextField(db_column='CSCODE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    startcheckupdate = models.TextField(db_column='STARTCHECKUPDATE', blank=True, null=True)  # Field name made lowercase.
    endcheckupdate = models.TextField(db_column='ENDCHECKUPDATE', blank=True, null=True)  # Field name made lowercase.
    sended = models.TextField(db_column='SENDED', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    finished = models.TextField(db_column='FINISHED', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    id_expert_base = models.TextField(db_column='ID_EXPERT_BASE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_import_expert_check_list'


class DataImportExpertCheckState(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    id_expert_base = models.TextField(db_column='ID_EXPERT_BASE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    state = models.TextField(db_column='STATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    currentgroupnum = models.TextField(db_column='CURRENTGROUPNUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    currentprojectnum = models.TextField(db_column='CURRENTPROJECTNUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    totalgroupnum = models.TextField(db_column='TOTALGROUPNUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    totalprojectnum = models.TextField(db_column='TOTALPROJECTNUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    willgroupnum = models.TextField(db_column='WILLGROUPNUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    willprojectnum = models.TextField(db_column='WILLPROJECTNUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_import_expert_check_state'


class DataImportExpertDesuetudeLog(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    id_expert_desuetude_log = models.TextField(db_column='ID_EXPERT_DESUETUDE_LOG')  # Field name made lowercase. This field type is a guess.
    id_expert_base = models.TextField(db_column='ID_EXPERT_BASE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    person = models.TextField(db_column='PERSON', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createtime = models.TextField(db_column='CREATETIME', blank=True, null=True)  # Field name made lowercase.
    papermaterial = models.TextField(db_column='PAPERMATERIAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    remark = models.TextField(db_column='REMARK', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_import_expert_desuetude_log'


class DataImportExpertFile(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    id_expert_file = models.TextField(db_column='ID_EXPERT_FILE')  # Field name made lowercase. This field type is a guess.
    rel_id = models.TextField(db_column='REL_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    path = models.TextField(db_column='PATH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dest_filename = models.TextField(db_column='DEST_FILENAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    file_name = models.TextField(db_column='FILE_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    type = models.TextField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_import_expert_file'


class DataImportExpertGrade(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    id_expert_grade = models.TextField(db_column='ID_EXPERT_GRADE')  # Field name made lowercase. This field type is a guess.
    appraisal_date = models.TextField(db_column='APPRAISAL_DATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ability_point = models.TextField(db_column='ABILITY_POINT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    id_expert_base = models.TextField(db_column='ID_EXPERT_BASE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_import_expert_grade'


class DataImportExpertOperationThanLog(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    id_expert_operation_log = models.TextField(db_column='ID_EXPERT_OPERATION_LOG')  # Field name made lowercase. This field type is a guess.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    time = models.TextField(db_column='TIME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    upoperation = models.TextField(db_column='UPOPERATION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_import_expert_operation_than_log'


class DataImportExpertPatent(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    id_expert_patent = models.TextField(db_column='ID_EXPERT_PATENT')  # Field name made lowercase. This field type is a guess.
    patent_name = models.TextField(db_column='PATENT_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    patent_domain = models.TextField(db_column='PATENT_DOMAIN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    patentee_seq = models.TextField(db_column='PATENTEE_SEQ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    country = models.TextField(db_column='COUNTRY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    patent_type = models.TextField(db_column='PATENT_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    register_date = models.TextField(db_column='REGISTER_DATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    application = models.TextField(db_column='APPLICATION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    id_expert_base = models.TextField(db_column='ID_EXPERT_BASE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ordernum = models.TextField(db_column='ORDERNUM')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_import_expert_patent'


class DataImportExpertSendLog(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    id_expert_send_log = models.TextField(db_column='ID_EXPERT_SEND_LOG')  # Field name made lowercase. This field type is a guess.
    sendname = models.TextField(db_column='SENDNAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sendmailinfo = models.TextField(db_column='SENDMAILINFO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sendmobileinfo = models.TextField(db_column='SENDMOBILEINFO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sendtime = models.TextField(db_column='SENDTIME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sendmail1 = models.TextField(db_column='SENDMAIL1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sendmail2 = models.TextField(db_column='SENDMAIL2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sendmail3 = models.TextField(db_column='SENDMAIL3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    status = models.TextField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_import_expert_send_log'


class DataImportJshtDjcExpert(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sex = models.TextField(db_column='SEX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    company = models.TextField(db_column='COMPANY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    position = models.TextField(db_column='POSITION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    document_number = models.TextField(db_column='DOCUMENT_NUMBER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mobile = models.TextField(db_column='MOBILE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_import_jsht_djc_expert'


class DataImportJshtGxkycExpert(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sex = models.TextField(db_column='SEX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    company = models.TextField(db_column='COMPANY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    position = models.TextField(db_column='POSITION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    document_number = models.TextField(db_column='DOCUMENT_NUMBER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mobile = models.TextField(db_column='MOBILE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_import_jsht_gxkyc_expert'


class DataImportJshtQsydwExpert(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sex = models.TextField(db_column='SEX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    company = models.TextField(db_column='COMPANY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    company2 = models.TextField(db_column='COMPANY2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    position = models.TextField(db_column='POSITION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    position2 = models.TextField(db_column='POSITION2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    document_number = models.TextField(db_column='DOCUMENT_NUMBER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mobile = models.TextField(db_column='MOBILE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mobile2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    company_phone = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_import_jsht_qsydw_expert'


class DataImportJshtZfjgExpert(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sex = models.TextField(db_column='SEX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    company = models.TextField(db_column='COMPANY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    position = models.TextField(db_column='POSITION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    document_number = models.TextField(db_column='DOCUMENT_NUMBER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mobile = models.TextField(db_column='MOBILE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mobile2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    company_phone = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_import_jsht_zfjg_expert'


class DataImportTask(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    id_expert_task = models.TextField(db_column='ID_EXPERT_TASK')  # Field name made lowercase. This field type is a guess.
    project_name = models.TextField(db_column='PROJECT_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    start_date = models.TextField(db_column='START_DATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    task_end_date = models.TextField(db_column='TASK_END_DATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stakeholder = models.TextField(db_column='STAKEHOLDER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fund = models.TextField(db_column='FUND', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    effect = models.TextField(db_column='EFFECT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    id_expert_base = models.TextField(db_column='ID_EXPERT_BASE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ordernum = models.TextField(db_column='ORDERNUM')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_import_task'


class Department(models.Model):
    dept_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    dept_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    dept_code = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'department'


class Downloadinfoconstract(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    info = models.TextField(db_column='Info')  # Field name made lowercase.
    area = models.TextField()  # This field type is a guess.
    tag = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'downloadinfoconstract'


class EnvAduitAccountTable(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    audit_id = models.TextField(db_column='AUDIT_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    account_year = models.TextField(db_column='ACCOUNT_YEAR', blank=True, null=True)  # Field name made lowercase.
    account_money = models.TextField(db_column='ACCOUNT_MONEY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_aduit_account_table'


class EnvAllHistorySupport(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    history_year = models.TextField(db_column='HISTORY_YEAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    doumcment_num = models.TextField(db_column='DOUMCMENT_NUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    case_type = models.TextField(db_column='CASE_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    org_code = models.TextField(db_column='ORG_CODE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    report_company = models.TextField(db_column='REPORT_COMPANY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_name = models.TextField(db_column='PROJECT_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pay_case = models.TextField(db_column='PAY_CASE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_charge = models.TextField(db_column='PROJECT_CHARGE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    service_type = models.TextField(db_column='SERVICE_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    accept_num = models.TextField(db_column='ACCEPT_NUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_all_history_support'


class EnvAnimalReviewTable(models.Model):
    review_id = models.TextField(db_column='REVIEW_ID', unique=True)  # Field name made lowercase. This field type is a guess.
    lead_opinion = models.TextField(db_column='LEAD_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    organization_opinion = models.TextField(db_column='ORGANIZATION_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    manager_opinion = models.TextField(db_column='MANAGER_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    employee_opinion = models.TextField(db_column='EMPLOYEE_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    labor_protection_opinion = models.TextField(db_column='LABOR_PROTECTION_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    external_environment_opinion = models.TextField(db_column='EXTERNAL_ENVIRONMENT_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    internal_environment_opinion = models.TextField(db_column='INTERNAL_ENVIRONMENT_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    layout_opinion = models.TextField(db_column='LAYOUT_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    retaining_structure_opinion = models.TextField(db_column='RETAINING_STRUCTURE_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    wallandceiling_opinion = models.TextField(db_column='WALLANDCEILING_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    floor_opinion = models.TextField(db_column='FLOOR_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    corridor_opinion = models.TextField(db_column='CORRIDOR_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    other = models.TextField(db_column='OTHER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_animal_review_table'


class EnvApprovalCollectInfo(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    approval_id = models.TextField(db_column='APPROVAL_ID')  # Field name made lowercase. This field type is a guess.
    project_id = models.TextField(db_column='PROJECT_ID')  # Field name made lowercase. This field type is a guess.
    project_name = models.TextField(db_column='PROJECT_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    high_tech_field = models.TextField(db_column='HIGH_TECH_FIELD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sub_high_tech_field = models.TextField(db_column='SUB_HIGH_TECH_FIELD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_type = models.TextField(db_column='PROJECT_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    research_content = models.TextField(db_column='RESEARCH_CONTENT', blank=True, null=True)  # Field name made lowercase.
    project_no = models.TextField(db_column='PROJECT_NO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    inspection_indicator = models.TextField(db_column='INSPECTION_INDICATOR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'env_approval_collect_info'


class EnvApprovalTable(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    undertake_opinion = models.TextField(db_column='UNDERTAKE_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    first_undertake_opinion = models.TextField(db_column='FIRST_UNDERTAKE_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    second_undertake_opinion = models.TextField(db_column='SECOND_UNDERTAKE_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    undertake_person_id = models.TextField(db_column='UNDERTAKE_PERSON_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    first_undertake_person_id = models.TextField(db_column='FIRST_UNDERTAKE_PERSON_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    second_undertake_person_id = models.TextField(db_column='SECOND_UNDERTAKE_PERSON_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    undertake_date = models.TextField(db_column='UNDERTAKE_DATE', blank=True, null=True)  # Field name made lowercase.
    first_undertake_date = models.TextField(db_column='FIRST_UNDERTAKE_DATE', blank=True, null=True)  # Field name made lowercase.
    second_undertake_date = models.TextField(db_column='SECOND_UNDERTAKE_DATE', blank=True, null=True)  # Field name made lowercase.
    undertake_result = models.TextField(db_column='UNDERTAKE_RESULT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    first_undertake_result = models.TextField(db_column='FIRST_UNDERTAKE_RESULT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    second_undertake_result = models.TextField(db_column='SECOND_UNDERTAKE_RESULT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    audit_opinion = models.TextField(db_column='AUDIT_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    audit_person_id = models.TextField(db_column='AUDIT_PERSON_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    audit_date = models.TextField(db_column='AUDIT_DATE', blank=True, null=True)  # Field name made lowercase.
    audit_result = models.TextField(db_column='AUDIT_RESULT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    approve_opinion = models.TextField(db_column='APPROVE_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    approve_person_id = models.TextField(db_column='APPROVE_PERSON_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    approve_date = models.TextField(db_column='APPROVE_DATE', blank=True, null=True)  # Field name made lowercase.
    approve_result = models.TextField(db_column='APPROVE_RESULT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    council_opinion = models.TextField(db_column='COUNCIL_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    council_date = models.TextField(db_column='COUNCIL_DATE', blank=True, null=True)  # Field name made lowercase.
    council_result = models.TextField(db_column='COUNCIL_RESULT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    joint_conference_result = models.TextField(db_column='JOINT_CONFERENCE_RESULT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    joint_conference_opinion = models.TextField(db_column='JOINT_CONFERENCE_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    status = models.TextField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    support_mode = models.TextField(db_column='SUPPORT_MODE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    support_budget = models.TextField(db_column='SUPPORT_BUDGET', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    finance_file_no = models.TextField(db_column='FINANCE_FILE_NO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_id = models.TextField(db_column='PROJECT_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    remark = models.TextField(db_column='REMARK', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    is_belong = models.TextField(db_column='IS_BELONG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    is_fit = models.TextField(db_column='IS_FIT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    is_fit_first = models.TextField(db_column='IS_FIT_FIRST', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    is_fit_second = models.TextField(db_column='IS_FIT_SECOND', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    undertake_person_name = models.TextField(db_column='UNDERTAKE_PERSON_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    first_undertake_person_name = models.TextField(db_column='FIRST_UNDERTAKE_PERSON_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    second_undertake_person_name = models.TextField(db_column='SECOND_UNDERTAKE_PERSON_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    audit_person_name = models.TextField(db_column='AUDIT_PERSON_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    approve_person_name = models.TextField(db_column='APPROVE_PERSON_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    is_intellectual_property_clear = models.TextField(db_column='IS_INTELLECTUAL_PROPERTY_CLEAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_situation = models.TextField(db_column='PROJECT_SITUATION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    goverment_type = models.TextField(db_column='GOVERMENT_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    undertake_suggest_budget = models.TextField(db_column='UNDERTAKE_SUGGEST_BUDGET', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    first_undertake_suggest_budget = models.TextField(db_column='FIRST_UNDERTAKE_SUGGEST_BUDGET', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    second_undertake_suggest_budget = models.TextField(db_column='SECOND_UNDERTAKE_SUGGEST_BUDGET', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fund_source = models.TextField(db_column='FUND_SOURCE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_budget = models.TextField(db_column='TOTAL_BUDGET', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fund_of_this = models.TextField(db_column='FUND_OF_THIS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    is_having_partner = models.TextField(db_column='IS_HAVING_PARTNER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    allocated_budget = models.TextField(db_column='ALLOCATED_BUDGET', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    committee_date = models.TextField(db_column='COMMITTEE_DATE', blank=True, null=True)  # Field name made lowercase.
    fname = models.TextField(db_column='FNAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sname = models.TextField(db_column='SNAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    implement_dead_line = models.TextField(db_column='IMPLEMENT_DEAD_LINE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    declare_dead_line = models.TextField(db_column='DECLARE_DEAD_LINE', blank=True, null=True)  # Field name made lowercase.
    support_budget2 = models.TextField(db_column='SUPPORT_BUDGET2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fund_of_next = models.TextField(db_column='FUND_OF_NEXT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fund_of_after_next = models.TextField(db_column='FUND_OF_AFTER_NEXT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    contract_type = models.TextField(db_column='CONTRACT_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    contract_amount = models.TextField(db_column='CONTRACT_AMOUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    is_first_withdraw = models.TextField(db_column='IS_FIRST_WITHDRAW', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    is_second_withdraw = models.TextField(db_column='IS_SECOND_WITHDRAW', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sustainable_result_one = models.TextField(db_column='SUSTAINABLE_RESULT_ONE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sustainable_result_two = models.TextField(db_column='SUSTAINABLE_RESULT_TWO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sustainable_result_three = models.TextField(db_column='SUSTAINABLE_RESULT_THREE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sustainable_result_four = models.TextField(db_column='SUSTAINABLE_RESULT_FOUR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sustainable_remark_one = models.TextField(db_column='SUSTAINABLE_REMARK_ONE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sustainable_remark_two = models.TextField(db_column='SUSTAINABLE_REMARK_TWO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sustainable_remark_three = models.TextField(db_column='SUSTAINABLE_REMARK_THREE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sustainable_remark_four = models.TextField(db_column='SUSTAINABLE_REMARK_FOUR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    first_undertake_remarks = models.TextField(db_column='FIRST_UNDERTAKE_REMARKS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    second_undertake_remarks = models.TextField(db_column='SECOND_UNDERTAKE_REMARKS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    audit_remarks = models.TextField(db_column='AUDIT_REMARKS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    approve_remarks = models.TextField(db_column='APPROVE_REMARKS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    council_remarks = models.TextField(db_column='COUNCIL_REMARKS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    council_name = models.TextField(db_column='COUNCIL_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    council_id = models.TextField(db_column='COUNCIL_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_approval_table'


class EnvAuditTable(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    project_id = models.TextField(db_column='PROJECT_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    audit_user_id = models.TextField(db_column='AUDIT_USER_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    review_type = models.TextField(db_column='REVIEW_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    account_firm_name = models.TextField(db_column='ACCOUNT_FIRM_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bussiness_year = models.TextField(db_column='BUSSINESS_YEAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    company_name = models.TextField(db_column='COMPANY_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_name = models.TextField(db_column='PROJECT_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    audit_content = models.TextField(db_column='AUDIT_CONTENT', blank=True, null=True)  # Field name made lowercase.
    company_base_info = models.TextField(db_column='COMPANY_BASE_INFO', blank=True, null=True)  # Field name made lowercase.
    audit_opinion = models.TextField(db_column='AUDIT_OPINION', blank=True, null=True)  # Field name made lowercase.
    organe_fee = models.TextField(db_column='ORGANE_FEE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    promotion_fee = models.TextField(db_column='PROMOTION_FEE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    meeting_fee = models.TextField(db_column='MEETING_FEE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    guest_fee = models.TextField(db_column='GUEST_FEE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    security_fee = models.TextField(db_column='SECURITY_FEE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    other_fee = models.TextField(db_column='OTHER_FEE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_fee = models.TextField(db_column='TOTAL_FEE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    audit_problem = models.TextField(db_column='AUDIT_PROBLEM', blank=True, null=True)  # Field name made lowercase.
    audit_company = models.TextField(db_column='AUDIT_COMPANY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    auditor = models.TextField(db_column='AUDITOR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    accountants = models.TextField(db_column='ACCOUNTANTS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    audit_time = models.TextField(db_column='AUDIT_TIME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    budget_number = models.TextField(db_column='BUDGET_NUMBER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    actual_expense_number = models.TextField(db_column='ACTUAL_EXPENSE_NUMBER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    financial_aid = models.TextField(db_column='FINANCIAL_AID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    audit_address = models.TextField(db_column='AUDIT_ADDRESS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    status = models.TextField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    submit_time = models.TextField(db_column='SUBMIT_TIME', blank=True, null=True)  # Field name made lowercase.
    execution_start_time = models.TextField(db_column='EXECUTION_START_TIME', blank=True, null=True)  # Field name made lowercase.
    execution_end_time = models.TextField(db_column='EXECUTION_END_TIME', blank=True, null=True)  # Field name made lowercase.
    total_amount = models.TextField(db_column='TOTAL_AMOUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    national_fund = models.TextField(db_column='NATIONAL_FUND', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    province_fund = models.TextField(db_column='PROVINCE_FUND', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    self_raised_fund = models.TextField(db_column='SELF_RAISED_FUND', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    have_support = models.TextField(db_column='HAVE_SUPPORT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    apply_support = models.TextField(db_column='APPLY_SUPPORT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    account_fund = models.TextField(db_column='ACCOUNT_FUND', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    joint_unit = models.TextField(db_column='JOINT_UNIT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    joint_unit_unallocate = models.TextField(db_column='JOINT_UNIT_UNALLOCATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    joint_unit_allocate = models.TextField(db_column='JOINT_UNIT_ALLOCATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    requirement = models.TextField(db_column='REQUIREMENT', blank=True, null=True)  # Field name made lowercase.
    register_type = models.TextField(db_column='REGISTER_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    register_capital = models.TextField(db_column='REGISTER_CAPITAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    register_date = models.TextField(db_column='REGISTER_DATE', blank=True, null=True)  # Field name made lowercase.
    represent_name = models.TextField(db_column='REPRESENT_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    principal_product = models.TextField(db_column='PRINCIPAL_PRODUCT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_start_time = models.TextField(db_column='PROJECT_START_TIME', blank=True, null=True)  # Field name made lowercase.
    project_end_time = models.TextField(db_column='PROJECT_END_TIME', blank=True, null=True)  # Field name made lowercase.
    plan_type = models.TextField(db_column='PLAN_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_depart = models.TextField(db_column='PROJECT_DEPART', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    match_ratio_require = models.TextField(db_column='MATCH_RATIO_REQUIRE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fund_depart = models.TextField(db_column='FUND_DEPART', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    issued_doc_number = models.TextField(db_column='ISSUED_DOC_NUMBER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cooperator1 = models.TextField(db_column='COOPERATOR1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cooperator2 = models.TextField(db_column='COOPERATOR2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cooperator3 = models.TextField(db_column='COOPERATOR3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cooperator4 = models.TextField(db_column='COOPERATOR4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cooperator5 = models.TextField(db_column='COOPERATOR5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    apply_total = models.TextField(db_column='APPLY_TOTAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    apply_total_acuumulate = models.TextField(db_column='APPLY_TOTAL_ACUUMULATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    apply_order = models.TextField(db_column='APPLY_ORDER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    apply_notissued = models.TextField(db_column='APPLY_NOTISSUED', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    coop_total = models.TextField(db_column='COOP_TOTAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    coop_total_acuumulate = models.TextField(db_column='COOP_TOTAL_ACUUMULATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    coop_order = models.TextField(db_column='COOP_ORDER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    coop_notissued = models.TextField(db_column='COOP_NOTISSUED', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    form_amount = models.TextField(db_column='FORM_AMOUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    support_amount = models.TextField(db_column='SUPPORT_AMOUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    this_support_amount = models.TextField(db_column='THIS_SUPPORT_AMOUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    match_ratio = models.TextField(db_column='MATCH_RATIO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spend_apply_number = models.TextField(db_column='SPEND_APPLY_NUMBER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    operate_expense = models.TextField(db_column='OPERATE_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    transfer_spend_apply_num = models.TextField(db_column='TRANSFER_SPEND_APPLY_NUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    transfer_spend_approval_num = models.TextField(db_column='TRANSFER_SPEND_APPROVAL_NUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    transfer_in_apply_num = models.TextField(db_column='TRANSFER_IN_APPLY_NUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    transfer_in_approval_num = models.TextField(db_column='TRANSFER_IN_APPROVAL_NUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_audit_table'


class EnvBusinessReviewTable(models.Model):
    review_id = models.TextField(db_column='REVIEW_ID', unique=True)  # Field name made lowercase. This field type is a guess.
    lead_opinion = models.TextField(db_column='LEAD_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    organization_opinion = models.TextField(db_column='ORGANIZATION_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    manager_opinion = models.TextField(db_column='MANAGER_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    employee_opinion = models.TextField(db_column='EMPLOYEE_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    labor_protection_opinion = models.TextField(db_column='LABOR_PROTECTION_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    external_environment_opinion = models.TextField(db_column='EXTERNAL_ENVIRONMENT_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    internal_environment_opinion = models.TextField(db_column='INTERNAL_ENVIRONMENT_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    layout_opinion = models.TextField(db_column='LAYOUT_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    retaining_structure_opinion = models.TextField(db_column='RETAINING_STRUCTURE_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    wallandceiling_opinion = models.TextField(db_column='WALLANDCEILING_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    floor_opinion = models.TextField(db_column='FLOOR_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    corridor_opinion = models.TextField(db_column='CORRIDOR_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    doorsandwindows_opinion = models.TextField(db_column='DOORSANDWINDOWS_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    activities_opinion = models.TextField(db_column='ACTIVITIES_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ventilation_system_opinion = models.TextField(db_column='VENTILATION_SYSTEM_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    drainage_opinion = models.TextField(db_column='DRAINAGE_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    electrical_opinion = models.TextField(db_column='ELECTRICAL_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    room_monitor_opinion = models.TextField(db_column='ROOM_MONITOR_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    animal_opinion = models.TextField(db_column='ANIMAL_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    feed_opinion = models.TextField(db_column='FEED_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bedding_opinion = models.TextField(db_column='BEDDING_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    drinking_water_opinion = models.TextField(db_column='DRINKING_WATER_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    basket_opinion = models.TextField(db_column='BASKET_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    animal_house_opinion = models.TextField(db_column='ANIMAL_HOUSE_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cage_instruments_opinion = models.TextField(db_column='CAGE_INSTRUMENTS_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    animal_welfare_opinion = models.TextField(db_column='ANIMAL_WELFARE_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    animals_kill_opinion = models.TextField(db_column='ANIMALS_KILL_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    waste_disposal_opinion = models.TextField(db_column='WASTE_DISPOSAL_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    animals_corpse_opinion = models.TextField(db_column='ANIMALS_CORPSE_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    special_animal_opinion = models.TextField(db_column='SPECIAL_ANIMAL_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    management_opinion = models.TextField(db_column='MANAGEMENT_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    laboratory_opinion = models.TextField(db_column='LABORATORY_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    emergency_measures_opinion = models.TextField(db_column='EMERGENCY_MEASURES_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    record_opinion = models.TextField(db_column='RECORD_OPINION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mechanism = models.TextField(db_column='MECHANISM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    personner = models.TextField(db_column='PERSONNER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    external = models.TextField(db_column='EXTERNAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    inside = models.TextField(db_column='INSIDE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    architecture = models.TextField(db_column='ARCHITECTURE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    environmental_indicator = models.TextField(db_column='ENVIRONMENTAL_INDICATOR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spf_level = models.TextField(db_column='SPF_LEVEL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    clean_level = models.TextField(db_column='CLEAN_LEVEL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ordinary_level = models.TextField(db_column='ORDINARY_LEVEL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    breeding_management = models.TextField(db_column='BREEDING_MANAGEMENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rules_regulations = models.TextField(db_column='RULES_REGULATIONS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    animal_experiment = models.TextField(db_column='ANIMAL_EXPERIMENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    review_report = models.TextField(db_column='REVIEW_REPORT', blank=True, null=True)  # Field name made lowercase.
    scope_application = models.TextField(db_column='SCOPE_APPLICATION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    application_explain = models.TextField(db_column='APPLICATION_EXPLAIN', blank=True, null=True)  # Field name made lowercase.
    production_open_system = models.TextField(db_column='PRODUCTION_OPEN_SYSTEM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    production_parclose_system = models.TextField(db_column='PRODUCTION_PARCLOSE_SYSTEM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    production_segregate_system = models.TextField(db_column='PRODUCTION_SEGREGATE_SYSTEM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    production_parclose_or_open = models.TextField(db_column='PRODUCTION_PARCLOSE_OR_OPEN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    work_services = models.TextField(db_column='WORK_SERVICES', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    exist_services_city = models.TextField(db_column='EXIST_SERVICES_CITY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    have_corporate_capacity = models.TextField(db_column='HAVE_CORPORATE_CAPACITY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    have_bad_record = models.TextField(db_column='HAVE_BAD_RECORD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    junior_college_scale = models.TextField(db_column='JUNIOR_COLLEGE_SCALE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    production_total_area = models.TextField(db_column='PRODUCTION_TOTAL_AREA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    income_scale = models.TextField(db_column='INCOME_SCALE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    service_outsourcing_scale = models.TextField(db_column='SERVICE_OUTSOURCING_SCALE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    have_internation_approve = models.TextField(db_column='HAVE_INTERNATION_APPROVE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hava_rd_ability = models.TextField(db_column='HAVA_RD_ABILITY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    have_special_ability = models.TextField(db_column='HAVE_SPECIAL_ABILITY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_oriented_one = models.TextField(db_column='PROJECT_ORIENTED_ONE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_oriented_two = models.TextField(db_column='PROJECT_ORIENTED_TWO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_oriented_three = models.TextField(db_column='PROJECT_ORIENTED_THREE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_innovation_one = models.TextField(db_column='PROJECT_INNOVATION_ONE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_innovation_two = models.TextField(db_column='PROJECT_INNOVATION_TWO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_innovation_therr = models.TextField(db_column='PROJECT_INNOVATION_THERR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_patent_one = models.TextField(db_column='PROJECT_PATENT_ONE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_patent_two = models.TextField(db_column='PROJECT_PATENT_TWO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_patent_three = models.TextField(db_column='PROJECT_PATENT_THREE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_change_one = models.TextField(db_column='PROJECT_CHANGE_ONE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_change_two = models.TextField(db_column='PROJECT_CHANGE_TWO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_change_three = models.TextField(db_column='PROJECT_CHANGE_THREE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_change_four = models.TextField(db_column='PROJECT_CHANGE_FOUR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_material_one = models.TextField(db_column='PROJECT_MATERIAL_ONE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_grade_all = models.TextField(db_column='PROJECT_GRADE_ALL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expert_conclusion = models.TextField(db_column='EXPERT_CONCLUSION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_oriented_score_one = models.TextField(db_column='PROJECT_ORIENTED_SCORE_ONE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_oriented_score_two = models.TextField(db_column='PROJECT_ORIENTED_SCORE_TWO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_oriented_score_three = models.TextField(db_column='PROJECT_ORIENTED_SCORE_THREE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_innovation_score_one = models.TextField(db_column='PROJECT_INNOVATION_SCORE_ONE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_innovation_score_two = models.TextField(db_column='PROJECT_INNOVATION_SCORE_TWO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_innovation_score_therr = models.TextField(db_column='PROJECT_INNOVATION_SCORE_THERR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_patent_score_one = models.TextField(db_column='PROJECT_PATENT_SCORE_ONE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_patent_score_two = models.TextField(db_column='PROJECT_PATENT_SCORE_TWO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_patent_score_three = models.TextField(db_column='PROJECT_PATENT_SCORE_THREE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_change_score_one = models.TextField(db_column='PROJECT_CHANGE_SCORE_ONE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_change_score_two = models.TextField(db_column='PROJECT_CHANGE_SCORE_TWO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_change_score_three = models.TextField(db_column='PROJECT_CHANGE_SCORE_THREE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_change_score_four = models.TextField(db_column='PROJECT_CHANGE_SCORE_FOUR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_material_score_one = models.TextField(db_column='PROJECT_MATERIAL_SCORE_ONE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_familiarity = models.TextField(db_column='PROJECT_FAMILIARITY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_business_review_table'


class EnvCertificateFinishTable(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    project_id = models.TextField(db_column='PROJECT_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    result = models.TextField(db_column='RESULT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    certificate_name = models.TextField(db_column='CERTIFICATE_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    certificate_id = models.TextField(db_column='CERTIFICATE_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    certificate_start_time = models.TextField(db_column='CERTIFICATE_START_TIME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    certificate_end_time = models.TextField(db_column='CERTIFICATE_END_TIME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    charge = models.TextField(db_column='CHARGE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    finished_time = models.TextField(db_column='FINISHED_TIME', blank=True, null=True)  # Field name made lowercase.
    finished_persion = models.TextField(db_column='FINISHED_PERSION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    status = models.TextField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    return_resion = models.TextField(db_column='RETURN_RESION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_certificate_finish_table'


class EnvCollectExpertInfo(models.Model):
    project_id = models.TextField(db_column='PROJECT_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    unitandduty = models.TextField(db_column='UNITANDDUTY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    phone = models.TextField(db_column='PHONE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    add_time = models.TextField(db_column='ADD_TIME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_collect_expert_info'


class EnvCollectInfo(models.Model):
    project_id = models.TextField(db_column='PROJECT_ID', unique=True)  # Field name made lowercase. This field type is a guess.
    plantype = models.TextField(db_column='PLANTYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    projecttype = models.TextField(db_column='PROJECTTYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    operation_time = models.TextField(db_column='OPERATION_TIME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    reject_times = models.TextField(db_column='REJECT_TIMES', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_collect_info'


class EnvCompanyAccessoryInfo(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    company_base_info_id = models.TextField(db_column='COMPANY_BASE_INFO_ID')  # Field name made lowercase. This field type is a guess.
    type = models.TextField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    file_id = models.TextField(db_column='FILE_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sequence = models.TextField(db_column='SEQUENCE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_company_accessory_info'


class EnvCompanyAccessoryInfoCopy(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    company_base_info_id = models.TextField(db_column='COMPANY_BASE_INFO_ID')  # Field name made lowercase. This field type is a guess.
    type = models.TextField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    file_id = models.TextField(db_column='FILE_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sequence = models.TextField(db_column='SEQUENCE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_company_accessory_info_copy'


class EnvCompanyBaseInfo(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    company_id = models.TextField(db_column='COMPANY_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    year = models.TextField(db_column='YEAR')  # Field name made lowercase. This field type is a guess.
    company_name = models.TextField(db_column='COMPANY_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    company_address = models.TextField(db_column='COMPANY_ADDRESS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    register_capital = models.TextField(db_column='REGISTER_CAPITAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    register_date = models.TextField(db_column='REGISTER_DATE', blank=True, null=True)  # Field name made lowercase.
    register_region = models.TextField(db_column='REGISTER_REGION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    register_street = models.TextField(db_column='REGISTER_STREET', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    office_region = models.TextField(db_column='OFFICE_REGION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    factory_region = models.TextField(db_column='FACTORY_REGION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    org_code = models.TextField(db_column='ORG_CODE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    license_code = models.TextField(db_column='LICENSE_CODE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    national_tax_code = models.TextField(db_column='NATIONAL_TAX_CODE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    local_tax_code = models.TextField(db_column='LOCAL_TAX_CODE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    deposit_bank = models.TextField(db_column='DEPOSIT_BANK', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    credit_degree = models.TextField(db_column='CREDIT_DEGREE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    deposit_bank_number = models.TextField(db_column='DEPOSIT_BANK_NUMBER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    register_type = models.TextField(db_column='REGISTER_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    website_url = models.TextField(db_column='WEBSITE_URL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    qualification = models.TextField(db_column='QUALIFICATION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    business_scope = models.TextField(db_column='BUSINESS_SCOPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    principal_product = models.TextField(db_column='PRINCIPAL_PRODUCT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    industry_type = models.TextField(db_column='INDUSTRY_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    industry_category = models.TextField(db_column='INDUSTRY_CATEGORY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    industry_kind = models.TextField(db_column='INDUSTRY_KIND', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    industry_small_kind = models.TextField(db_column='INDUSTRY_SMALL_KIND', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    high_tech_field = models.TextField(db_column='HIGH_TECH_FIELD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    high_tech_subfield = models.TextField(db_column='HIGH_TECH_SUBFIELD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    research_office_space = models.TextField(db_column='RESEARCH_OFFICE_SPACE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    factory_space = models.TextField(db_column='FACTORY_SPACE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    offshore_sales_unit_count = models.TextField(db_column='OFFSHORE_SALES_UNIT_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    offshore_resarch_unit_count = models.TextField(db_column='OFFSHORE_RESARCH_UNIT_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    year_power_consumption = models.TextField(db_column='YEAR_POWER_CONSUMPTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    year_water_consumption = models.TextField(db_column='YEAR_WATER_CONSUMPTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stock_exchange = models.TextField(db_column='STOCK_EXCHANGE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ipo_date = models.TextField(db_column='IPO_DATE', blank=True, null=True)  # Field name made lowercase.
    stock_code = models.TextField(db_column='STOCK_CODE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_eployee_count = models.TextField(db_column='TOTAL_EPLOYEE_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    male_eployee_count = models.TextField(db_column='MALE_EPLOYEE_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    female_eployee_count = models.TextField(db_column='FEMALE_EPLOYEE_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    social_insurance_eployee_count = models.TextField(db_column='SOCIAL_INSURANCE_EPLOYEE_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    returned_student_count = models.TextField(db_column='RETURNED_STUDENT_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    foreign_expert_count = models.TextField(db_column='FOREIGN_EXPERT_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    graduate_count = models.TextField(db_column='GRADUATE_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hr_eployee_count = models.TextField(db_column='HR_EPLOYEE_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sales_eployee_count = models.TextField(db_column='SALES_EPLOYEE_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rd_eployee_count = models.TextField(db_column='RD_EPLOYEE_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    manufacture_eployee_count = models.TextField(db_column='MANUFACTURE_EPLOYEE_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    other_job_count = models.TextField(db_column='OTHER_JOB_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    doctor_eployee_count = models.TextField(db_column='DOCTOR_EPLOYEE_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    master_eployee_count = models.TextField(db_column='MASTER_EPLOYEE_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    undergraduate_eployee_count = models.TextField(db_column='UNDERGRADUATE_EPLOYEE_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    junior_college_eployee_count = models.TextField(db_column='JUNIOR_COLLEGE_EPLOYEE_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otehr_degree_eployee_count = models.TextField(db_column='OTEHR_DEGREE_EPLOYEE_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sinior_eployee_professor = models.TextField(db_column='SINIOR_EPLOYEE_PROFESSOR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    midium_eployee_professor = models.TextField(db_column='MIDIUM_EPLOYEE_PROFESSOR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    junior_eployee_professor = models.TextField(db_column='JUNIOR_EPLOYEE_PROFESSOR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    other_title_eployee_professor = models.TextField(db_column='OTHER_TITLE_EPLOYEE_PROFESSOR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    icp_license_number = models.TextField(db_column='ICP_LICENSE_NUMBER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isp_license_number = models.TextField(db_column='ISP_LICENSE_NUMBER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    paicl_up_capital = models.TextField(db_column='PAICL_UP_CAPITAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    corporate_representative_major = models.TextField(db_column='CORPORATE_REPRESENTATIVE_MAJOR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    corporate_representative_resume = models.TextField(db_column='CORPORATE_REPRESENTATIVE_RESUME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    institution_introduction = models.TextField(db_column='INSTITUTION_INTRODUCTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_net_cashflow = models.TextField(db_column='TOTAL_NET_CASHFLOW', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    operation_net_cashflow = models.TextField(db_column='OPERATION_NET_CASHFLOW', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sales_income = models.TextField(db_column='SALES_INCOME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    promotion_expense = models.TextField(db_column='PROMOTION_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    governmnet_loan = models.TextField(db_column='GOVERNMNET_LOAN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    matured_governmnet_loan = models.TextField(db_column='MATURED_GOVERNMNET_LOAN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    summary = models.TextField(db_column='SUMMARY', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    version = models.TextField(db_column='VERSION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    submitdate = models.TextField(db_column='SUBMITDATE', blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.TextField(db_column='LASTMODIFIED', blank=True, null=True)  # Field name made lowercase.
    item_year = models.TextField(db_column='ITEM_YEAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    contact_person = models.TextField(db_column='CONTACT_PERSON', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    contact_mobile = models.TextField(db_column='CONTACT_MOBILE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    remark = models.TextField(db_column='REMARK', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    open_start_time = models.TextField(db_column='OPEN_START_TIME', blank=True, null=True)  # Field name made lowercase.
    open_end_time = models.TextField(db_column='OPEN_END_TIME', blank=True, null=True)  # Field name made lowercase.
    zwdtsw_user_id = models.TextField(db_column='ZWDTSW_USER_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_company_base_info'


class EnvCompanyEployeeInfo(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    company_base_info_id = models.TextField(db_column='COMPANY_BASE_INFO_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    title = models.TextField(db_column='TITLE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mobile = models.TextField(db_column='MOBILE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    education_degree = models.TextField(db_column='EDUCATION_DEGREE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    security_id = models.TextField(db_column='SECURITY_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    email = models.TextField(db_column='EMAIL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    positional_title = models.TextField(db_column='POSITIONAL_TITLE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    post = models.TextField(db_column='POST', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_company_eployee_info'


class EnvCompanyFinanceInfo(models.Model):
    company_base_info_id = models.TextField(db_column='COMPANY_BASE_INFO_ID', unique=True)  # Field name made lowercase. This field type is a guess.
    total_income = models.TextField(db_column='TOTAL_INCOME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    main_income = models.TextField(db_column='MAIN_INCOME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    high_tech_product_income = models.TextField(db_column='HIGH_TECH_PRODUCT_INCOME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    software_product_income = models.TextField(db_column='SOFTWARE_PRODUCT_INCOME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_industrial_value = models.TextField(db_column='TOTAL_INDUSTRIAL_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    high_tech_product_value = models.TextField(db_column='HIGH_TECH_PRODUCT_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pro_int_right_value = models.TextField(db_column='PRO_INT_RIGHT_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_increase_value = models.TextField(db_column='TOTAL_INCREASE_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    employee_rem_increase_value = models.TextField(db_column='EMPLOYEE_REM_INCREASE_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dep_fix_assets_value = models.TextField(db_column='DEP_FIX_ASSETS_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    manufacture_net_tax = models.TextField(db_column='MANUFACTURE_NET_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    operation_net_value = models.TextField(db_column='OPERATION_NET_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_export_value = models.TextField(db_column='TOTAL_EXPORT_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    high_tech_export_value = models.TextField(db_column='HIGH_TECH_EXPORT_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    net_margin = models.TextField(db_column='NET_MARGIN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_tax = models.TextField(db_column='TOTAL_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    value_added_tax = models.TextField(db_column='VALUE_ADDED_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    operation_tax = models.TextField(db_column='OPERATION_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    income_tax = models.TextField(db_column='INCOME_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    personal_income_tax = models.TextField(db_column='PERSONAL_INCOME_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    other_tax = models.TextField(db_column='OTHER_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_relief_tax = models.TextField(db_column='TOTAL_RELIEF_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    relief_value_added_tax = models.TextField(db_column='RELIEF_VALUE_ADDED_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    relief_operation_tax = models.TextField(db_column='RELIEF_OPERATION_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    relief_income_tax = models.TextField(db_column='RELIEF_INCOME_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    relief_jjkc_tax = models.TextField(db_column='RELIEF_JJKC_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    relief_high_tech_pro_tax = models.TextField(db_column='RELIEF_HIGH_TECH_PRO_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_assets = models.TextField(db_column='TOTAL_ASSETS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_liability = models.TextField(db_column='TOTAL_LIABILITY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_fixed_assets = models.TextField(db_column='TOTAL_FIXED_ASSETS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fixed_assets_investment = models.TextField(db_column='FIXED_ASSETS_INVESTMENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rd_expense = models.TextField(db_column='RD_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    new_genery_income = models.TextField(db_column='NEW_GENERY_INCOME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    env_pro_income = models.TextField(db_column='ENV_PRO_INCOME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    financial_appropriation = models.TextField(db_column='FINANCIAL_APPROPRIATION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    operation_income = models.TextField(db_column='OPERATION_INCOME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tech_act_income = models.TextField(db_column='TECH_ACT_INCOME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tech_prov_act_income = models.TextField(db_column='TECH_PROV_ACT_INCOME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tech_muni_act_income = models.TextField(db_column='TECH_MUNI_ACT_INCOME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tech_other_act_income = models.TextField(db_column='TECH_OTHER_ACT_INCOME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    other_income = models.TextField(db_column='OTHER_INCOME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    income_inscrease_ratio = models.TextField(db_column='INCOME_INSCREASE_RATIO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_expense = models.TextField(db_column='TOTAL_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    operation_expense = models.TextField(db_column='OPERATION_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tech_act_expense = models.TextField(db_column='TECH_ACT_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tech_other_expense = models.TextField(db_column='TECH_OTHER_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_fix_assets_org_value = models.TextField(db_column='TOTAL_FIX_ASSETS_ORG_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_rd_property_value = models.TextField(db_column='TOTAL_RD_PROPERTY_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_rd_equipment_value = models.TextField(db_column='TOTAL_RD_EQUIPMENT_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_other_fix_assets_org_value = models.TextField(db_column='TOTAL_OTHER_FIX_ASSETS_ORG_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fix_assets_inscrease_ratio = models.TextField(db_column='FIX_ASSETS_INSCREASE_RATIO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rd_equipment_inscrease_ratio = models.TextField(db_column='RD_EQUIPMENT_INSCREASE_RATIO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_cash_balance = models.TextField(db_column='TOTAL_CASH_BALANCE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_debt_capital = models.TextField(db_column='TOTAL_DEBT_CAPITAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    env_protected_income = models.TextField(db_column='ENV_PROTECTED_INCOME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    org_code = models.TextField(db_column='ORG_CODE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item_year = models.TextField(db_column='ITEM_YEAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pay_salary_income_total = models.TextField(db_column='PAY_SALARY_INCOME_TOTAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    high_tech_product_service_income = models.TextField(db_column='HIGH_TECH_PRODUCT_SERVICE_INCOME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    major_support_income_tax_relief = models.TextField(db_column='MAJOR_SUPPORT_INCOME_TAX_RELIEF', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tech_transport_income_tax_relief = models.TextField(db_column='TECH_TRANSPORT_INCOME_TAX_RELIEF', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    other_pref_tax = models.TextField(db_column='OTHER_PREF_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    company_income_tax = models.TextField(db_column='COMPANY_INCOME_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_company_finance_info'


class EnvCompanyFundHistory(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    company_id = models.TextField(db_column='COMPANY_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_name = models.TextField(db_column='PROJECT_NAME')  # Field name made lowercase. This field type is a guess.
    sponsor = models.TextField(db_column='SPONSOR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    approved_date = models.TextField(db_column='APPROVED_DATE', blank=True, null=True)  # Field name made lowercase.
    amount = models.TextField(db_column='AMOUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    has_accepted = models.TextField(db_column='HAS_ACCEPTED', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_content = models.TextField(db_column='PROJECT_CONTENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_company_fund_history'


class EnvCompanyMonthlyReport(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    group_id = models.TextField(db_column='GROUP_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_income = models.TextField(db_column='TOTAL_INCOME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    main_income = models.TextField(db_column='MAIN_INCOME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    high_tech_product_income = models.TextField(db_column='HIGH_TECH_PRODUCT_INCOME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    software_product_income = models.TextField(db_column='SOFTWARE_PRODUCT_INCOME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_industrial_value = models.TextField(db_column='TOTAL_INDUSTRIAL_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    high_tech_product_value = models.TextField(db_column='HIGH_TECH_PRODUCT_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_increase_value = models.TextField(db_column='TOTAL_INCREASE_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    employee_rem_increase_value = models.TextField(db_column='EMPLOYEE_REM_INCREASE_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dep_fix_assets_value = models.TextField(db_column='DEP_FIX_ASSETS_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    operation_margin = models.TextField(db_column='OPERATION_MARGIN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_tax = models.TextField(db_column='TOTAL_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    value_added_tax = models.TextField(db_column='VALUE_ADDED_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    income_tax = models.TextField(db_column='INCOME_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    operation_tax = models.TextField(db_column='OPERATION_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    net_margin = models.TextField(db_column='NET_MARGIN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    high_tech_protected_net_margin = models.TextField(db_column='HIGH_TECH_PROTECTED_NET_MARGIN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tech_relief_input = models.TextField(db_column='TECH_RELIEF_INPUT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_export_value = models.TextField(db_column='TOTAL_EXPORT_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    high_tech_export_value = models.TextField(db_column='HIGH_TECH_EXPORT_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item_date = models.TextField(db_column='ITEM_DATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item_month = models.TextField(db_column='ITEM_MONTH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item_year = models.TextField(db_column='ITEM_YEAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    org_code = models.TextField(db_column='ORG_CODE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_company_monthly_report'


class EnvCompanyMonthlyReportAddtionalInfo(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    group_id = models.TextField(db_column='GROUP_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    informant = models.TextField(db_column='INFORMANT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    informant_mobile = models.TextField(db_column='INFORMANT_MOBILE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item_year = models.TextField(db_column='ITEM_YEAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    org_code = models.TextField(db_column='ORG_CODE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    status = models.TextField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_company_monthly_report_addtional_info'


class EnvCompanyMonthlyReportFilter(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    group_id = models.TextField(db_column='GROUP_ID')  # Field name made lowercase. This field type is a guess.
    item_year = models.TextField(db_column='ITEM_YEAR')  # Field name made lowercase. This field type is a guess.
    index_value_jan = models.TextField(db_column='INDEX_VALUE_JAN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    index_value_feb = models.TextField(db_column='INDEX_VALUE_FEB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    index_value_mar = models.TextField(db_column='INDEX_VALUE_MAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    index_value_apr = models.TextField(db_column='INDEX_VALUE_APR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    index_value_may = models.TextField(db_column='INDEX_VALUE_MAY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    index_value_jun = models.TextField(db_column='INDEX_VALUE_JUN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    index_value_jul = models.TextField(db_column='INDEX_VALUE_JUL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    index_value_aug = models.TextField(db_column='INDEX_VALUE_AUG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    index_value_sep = models.TextField(db_column='INDEX_VALUE_SEP', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    index_value_oct = models.TextField(db_column='INDEX_VALUE_OCT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    index_value_nov = models.TextField(db_column='INDEX_VALUE_NOV', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    index_value_dec = models.TextField(db_column='INDEX_VALUE_DEC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    index_value_all = models.TextField(db_column='INDEX_VALUE_ALL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    index_value = models.TextField(db_column='INDEX_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_company_monthly_report_filter'


class EnvCompanyRdInfo(models.Model):
    company_base_info_id = models.TextField(db_column='COMPANY_BASE_INFO_ID', unique=True)  # Field name made lowercase. This field type is a guess.
    app_patent = models.TextField(db_column='APP_PATENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    app_pra_patent = models.TextField(db_column='APP_PRA_PATENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    app_sur_patent = models.TextField(db_column='APP_SUR_PATENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    own_patent = models.TextField(db_column='OWN_PATENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    own_pra_patent = models.TextField(db_column='OWN_PRA_PATENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    own_sur_patent = models.TextField(db_column='OWN_SUR_PATENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pub_paper = models.TextField(db_column='PUB_PAPER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pub_tech_paper = models.TextField(db_column='PUB_TECH_PAPER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    own_software = models.TextField(db_column='OWN_SOFTWARE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    own_ic_layout = models.TextField(db_column='OWN_IC_LAYOUT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    own_brand = models.TextField(db_column='OWN_BRAND', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    int_tech_stan = models.TextField(db_column='INT_TECH_STAN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    discover_plant = models.TextField(db_column='DISCOVER_PLANT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    own_medicine_cert = models.TextField(db_column='OWN_MEDICINE_CERT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nat_high_tech_reward = models.TextField(db_column='NAT_HIGH_TECH_REWARD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nat_key_lab = models.TextField(db_column='NAT_KEY_LAB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nat_engineering_center = models.TextField(db_column='NAT_ENGINEERING_CENTER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nat_project = models.TextField(db_column='NAT_PROJECT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    national_subsidization = models.TextField(db_column='NATIONAL_SUBSIDIZATION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    provincial_subsidization = models.TextField(db_column='PROVINCIAL_SUBSIDIZATION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    municipal_subsidization = models.TextField(db_column='MUNICIPAL_SUBSIDIZATION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nat_tech_stan = models.TextField(db_column='NAT_TECH_STAN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ind_tech_stan = models.TextField(db_column='IND_TECH_STAN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pro_high_tech_reward = models.TextField(db_column='PRO_HIGH_TECH_REWARD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mun_high_tech_reward = models.TextField(db_column='MUN_HIGH_TECH_REWARD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pro_key_lab = models.TextField(db_column='PRO_KEY_LAB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mun_key_lab = models.TextField(db_column='MUN_KEY_LAB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pro_engineering_center = models.TextField(db_column='PRO_ENGINEERING_CENTER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mun_engineering_center = models.TextField(db_column='MUN_ENGINEERING_CENTER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pro_project = models.TextField(db_column='PRO_PROJECT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mun_project = models.TextField(db_column='MUN_PROJECT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    authorised_software = models.TextField(db_column='AUTHORISED_SOFTWARE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item_year = models.TextField(db_column='ITEM_YEAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    org_code = models.TextField(db_column='ORG_CODE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_company_rd_info'


class EnvCompanyStockholderInfo(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    company_base_info_id = models.TextField(db_column='COMPANY_BASE_INFO_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    invest_amount = models.TextField(db_column='INVEST_AMOUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    invest_type = models.TextField(db_column='INVEST_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    invest_ratio = models.TextField(db_column='INVEST_RATIO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    id_card = models.TextField(db_column='ID_CARD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    citizen_type = models.TextField(db_column='CITIZEN_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_company_stockholder_info'


class EnvContractBaseInfo(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    project_id = models.TextField(db_column='PROJECT_ID')  # Field name made lowercase. This field type is a guess.
    company_base_info_id = models.TextField(db_column='COMPANY_BASE_INFO_ID')  # Field name made lowercase. This field type is a guess.
    contract_num = models.TextField(db_column='CONTRACT_NUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    contract_type = models.TextField(db_column='CONTRACT_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_invest_company = models.TextField(db_column='TOTAL_INVEST_COMPANY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_invest = models.TextField(db_column='TOTAL_INVEST', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    third_represent = models.TextField(db_column='THIRD_REPRESENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    third_project_resonser = models.TextField(db_column='THIRD_PROJECT_RESONSER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    third_resonser_contact = models.TextField(db_column='THIRD_RESONSER_CONTACT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    create_time = models.TextField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    create_user = models.TextField(db_column='CREATE_USER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    status = models.TextField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    officer_opinion = models.TextField(db_column='OFFICER_OPINION', blank=True, null=True)  # Field name made lowercase.
    fund_type = models.TextField(db_column='FUND_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    first_part = models.TextField(db_column='FIRST_PART', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    second_part = models.TextField(db_column='SECOND_PART', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    third_part = models.TextField(db_column='THIRD_PART', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_fund = models.TextField(db_column='PROJECT_FUND', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_fund_low = models.TextField(db_column='PROJECT_FUND_LOW', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    second_project_fund = models.TextField(db_column='SECOND_PROJECT_FUND', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    second_fund_year_after = models.TextField(db_column='SECOND_FUND_YEAR_AFTER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    second_fund_next_year = models.TextField(db_column='SECOND_FUND_NEXT_YEAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    second_fund_this_year = models.TextField(db_column='SECOND_FUND_THIS_YEAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    second_project_fund_low = models.TextField(db_column='SECOND_PROJECT_FUND_LOW', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    third_fund_this_year = models.TextField(db_column='THIRD_FUND_THIS_YEAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    third_fund_next_year = models.TextField(db_column='THIRD_FUND_NEXT_YEAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    third_fund_year_after = models.TextField(db_column='THIRD_FUND_YEAR_AFTER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    third_project_fund = models.TextField(db_column='THIRD_PROJECT_FUND', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    third_project_fund_low = models.TextField(db_column='THIRD_PROJECT_FUND_LOW', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    second_bank_name = models.TextField(db_column='SECOND_BANK_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    second_bank_number = models.TextField(db_column='SECOND_BANK_NUMBER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    third_bank_name = models.TextField(db_column='THIRD_BANK_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    third_bank_number = models.TextField(db_column='THIRD_BANK_NUMBER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    contract_start_time = models.TextField(db_column='CONTRACT_START_TIME', blank=True, null=True)  # Field name made lowercase.
    contract_end_time = models.TextField(db_column='CONTRACT_END_TIME', blank=True, null=True)  # Field name made lowercase.
    contract_create_time = models.TextField(db_column='CONTRACT_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    second_sign_time = models.TextField(db_column='SECOND_SIGN_TIME', blank=True, null=True)  # Field name made lowercase.
    third_sign_time = models.TextField(db_column='THIRD_SIGN_TIME', blank=True, null=True)  # Field name made lowercase.
    second_main_task = models.TextField(db_column='SECOND_MAIN_TASK', blank=True, null=True)  # Field name made lowercase.
    third_main_task = models.TextField(db_column='THIRD_MAIN_TASK', blank=True, null=True)  # Field name made lowercase.
    finish_level = models.TextField(db_column='FINISH_LEVEL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expert_display_type = models.TextField(db_column='EXPERT_DISPLAY_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expert_add_employment = models.TextField(db_column='EXPERT_ADD_EMPLOYMENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expert_cultivate_docs = models.TextField(db_column='EXPERT_CULTIVATE_DOCS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expert_cultivate_masters = models.TextField(db_column='EXPERT_CULTIVATE_MASTERS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expert_cultivate_engineers = models.TextField(db_column='EXPERT_CULTIVATE_ENGINEERS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expert_cultivate_workers = models.TextField(db_column='EXPERT_CULTIVATE_WORKERS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expert_profits = models.TextField(db_column='EXPERT_PROFITS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_sales = models.TextField(db_column='TOTAL_SALES', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expert_tax = models.TextField(db_column='EXPERT_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expert_money_input = models.TextField(db_column='EXPERT_MONEY_INPUT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expert_apply_invention = models.TextField(db_column='EXPERT_APPLY_INVENTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expert_apply_utility = models.TextField(db_column='EXPERT_APPLY_UTILITY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expert_apply_model = models.TextField(db_column='EXPERT_APPLY_MODEL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expert_author_invention = models.TextField(db_column='EXPERT_AUTHOR_INVENTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expert_author_utility = models.TextField(db_column='EXPERT_AUTHOR_UTILITY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expert_author_model = models.TextField(db_column='EXPERT_AUTHOR_MODEL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expert_publish_papers = models.TextField(db_column='EXPERT_PUBLISH_PAPERS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expert_publish_sci = models.TextField(db_column='EXPERT_PUBLISH_SCI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expert_publish_ei = models.TextField(db_column='EXPERT_PUBLISH_EI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expert_monograph_dometic = models.TextField(db_column='EXPERT_MONOGRAPH_DOMETIC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expert_monograph_foreign = models.TextField(db_column='EXPERT_MONOGRAPH_FOREIGN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    complete_effect = models.TextField(db_column='COMPLETE_EFFECT', blank=True, null=True)  # Field name made lowercase.
    performance_rax = models.TextField(db_column='PERFORMANCE_RAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    all_budget_remark = models.TextField(db_column='ALL_BUDGET_REMARK', blank=True, null=True)  # Field name made lowercase.
    all_amount_use = models.TextField(db_column='ALL_AMOUNT_USE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    second_budget_remark = models.TextField(db_column='SECOND_BUDGET_REMARK', blank=True, null=True)  # Field name made lowercase.
    third_budget_remark = models.TextField(db_column='THIRD_BUDGET_REMARK', blank=True, null=True)  # Field name made lowercase.
    equip_purchase_cost = models.TextField(db_column='EQUIP_PURCHASE_COST', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    equip_trial_cost = models.TextField(db_column='EQUIP_TRIAL_COST', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    equip_all_cost = models.TextField(db_column='EQUIP_ALL_COST', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    equip_remark = models.TextField(db_column='EQUIP_REMARK', blank=True, null=True)  # Field name made lowercase.
    incubation_area = models.TextField(db_column='INCUBATION_AREA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bear_form = models.TextField(db_column='BEAR_FORM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_name = models.TextField(db_column='PROJECT_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    company_name = models.TextField(db_column='COMPANY_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    contact_persion = models.TextField(db_column='CONTACT_PERSION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    contact_mobile = models.TextField(db_column='CONTACT_MOBILE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    company_submit_time = models.TextField(db_column='COMPANY_SUBMIT_TIME', blank=True, null=True)  # Field name made lowercase.
    second_part_manager = models.TextField(db_column='SECOND_PART_MANAGER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    second_part_mobile = models.TextField(db_column='SECOND_PART_MOBILE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    second_part_addr = models.TextField(db_column='SECOND_PART_ADDR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    office_charge_person = models.TextField(db_column='OFFICE_CHARGE_PERSON', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_charge_person = models.TextField(db_column='PROJECT_CHARGE_PERSON', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_charge_phone = models.TextField(db_column='PROJECT_CHARGE_PHONE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    second_part_legal_person = models.TextField(db_column='SECOND_PART_LEGAL_PERSON', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    second_part_legal_mobile = models.TextField(db_column='SECOND_PART_LEGAL_MOBILE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    third_part_legal_person = models.TextField(db_column='THIRD_PART_LEGAL_PERSON', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    third_part_legal_mobile = models.TextField(db_column='THIRD_PART_LEGAL_MOBILE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    third_part_manager = models.TextField(db_column='THIRD_PART_MANAGER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    third_part_mobile = models.TextField(db_column='THIRD_PART_MOBILE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    peacock_team_name = models.TextField(db_column='PEACOCK_TEAM_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    team_member_names = models.TextField(db_column='TEAM_MEMBER_NAMES', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    gj_contract_start_time = models.TextField(db_column='GJ_CONTRACT_START_TIME', blank=True, null=True)  # Field name made lowercase.
    gj_contract_end_time = models.TextField(db_column='GJ_CONTRACT_END_TIME', blank=True, null=True)  # Field name made lowercase.
    return_rate_third = models.TextField(db_column='RETURN_RATE_THIRD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    invest_amount_third = models.TextField(db_column='INVEST_AMOUNT_THIRD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    period_hold_first = models.TextField(db_column='PERIOD_HOLD_FIRST', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    equity_first = models.TextField(db_column='EQUITY_FIRST', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    plan_category = models.TextField(db_column='PLAN_CATEGORY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    superior_depart = models.TextField(db_column='SUPERIOR_DEPART', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    finance_file_no = models.TextField(db_column='FINANCE_FILE_NO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_contract_base_info'


class EnvContractEquipmentInfo(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    contract_id = models.TextField(db_column='CONTRACT_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.TextField(db_column='NAME')  # Field name made lowercase. This field type is a guess.
    equipment_type = models.TextField(db_column='EQUIPMENT_TYPE')  # Field name made lowercase. This field type is a guess.
    amount = models.TextField(db_column='AMOUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    unit = models.TextField(db_column='UNIT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    price = models.TextField(db_column='PRICE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total = models.TextField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_contract_equipment_info'


class EnvContractFund(models.Model):
    contract_id = models.TextField(db_column='CONTRACT_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sponsor = models.TextField(db_column='SPONSOR')  # Field name made lowercase. This field type is a guess.
    direct_expense = models.TextField(db_column='DIRECT_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    equipment_expense = models.TextField(db_column='EQUIPMENT_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buy_equ_expense = models.TextField(db_column='BUY_EQU_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    design_equ_expense = models.TextField(db_column='DESIGN_EQU_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rent_equ_expense = models.TextField(db_column='RENT_EQU_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    material_expense = models.TextField(db_column='MATERIAL_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    test_expense = models.TextField(db_column='TEST_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fuel_expense = models.TextField(db_column='FUEL_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    travel_expense = models.TextField(db_column='TRAVEL_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    meeting_expense = models.TextField(db_column='MEETING_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    coooperation_exchange_expense = models.TextField(db_column='COOOPERATION_EXCHANGE_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    transaction_expense = models.TextField(db_column='TRANSACTION_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    service_expense = models.TextField(db_column='SERVICE_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expect_con_expense = models.TextField(db_column='EXPECT_CON_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    staff_expense = models.TextField(db_column='STAFF_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    other_expense = models.TextField(db_column='OTHER_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    indirect_expense = models.TextField(db_column='INDIRECT_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    water_gas_expense = models.TextField(db_column='WATER_GAS_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    management_expense = models.TextField(db_column='MANAGEMENT_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    performance_reword = models.TextField(db_column='PERFORMANCE_REWORD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    region_trial_expense = models.TextField(db_column='REGION_TRIAL_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    other_description = models.TextField(db_column='OTHER_DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    enginerring_expense = models.TextField(db_column='ENGINERRING_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_expense = models.TextField(db_column='TOTAL_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    part_type = models.TextField(db_column='PART_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_contract_fund'


class EnvContractFundRemark(models.Model):
    contract_id = models.TextField(db_column='CONTRACT_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sponsor = models.TextField(db_column='SPONSOR')  # Field name made lowercase. This field type is a guess.
    direct_expense = models.TextField(db_column='DIRECT_EXPENSE', blank=True, null=True)  # Field name made lowercase.
    equipment_expense = models.TextField(db_column='EQUIPMENT_EXPENSE', blank=True, null=True)  # Field name made lowercase.
    buy_equ_expense = models.TextField(db_column='BUY_EQU_EXPENSE', blank=True, null=True)  # Field name made lowercase.
    design_equ_expense = models.TextField(db_column='DESIGN_EQU_EXPENSE', blank=True, null=True)  # Field name made lowercase.
    rent_equ_expense = models.TextField(db_column='RENT_EQU_EXPENSE', blank=True, null=True)  # Field name made lowercase.
    material_expense = models.TextField(db_column='MATERIAL_EXPENSE', blank=True, null=True)  # Field name made lowercase.
    test_expense = models.TextField(db_column='TEST_EXPENSE', blank=True, null=True)  # Field name made lowercase.
    fuel_expense = models.TextField(db_column='FUEL_EXPENSE', blank=True, null=True)  # Field name made lowercase.
    travel_expense = models.TextField(db_column='TRAVEL_EXPENSE', blank=True, null=True)  # Field name made lowercase.
    meeting_expense = models.TextField(db_column='MEETING_EXPENSE', blank=True, null=True)  # Field name made lowercase.
    coooperation_exchange_expense = models.TextField(db_column='COOOPERATION_EXCHANGE_EXPENSE', blank=True, null=True)  # Field name made lowercase.
    transaction_expense = models.TextField(db_column='TRANSACTION_EXPENSE', blank=True, null=True)  # Field name made lowercase.
    service_expense = models.TextField(db_column='SERVICE_EXPENSE', blank=True, null=True)  # Field name made lowercase.
    expect_con_expense = models.TextField(db_column='EXPECT_CON_EXPENSE', blank=True, null=True)  # Field name made lowercase.
    staff_expense = models.TextField(db_column='STAFF_EXPENSE', blank=True, null=True)  # Field name made lowercase.
    other_expense = models.TextField(db_column='OTHER_EXPENSE', blank=True, null=True)  # Field name made lowercase.
    indirect_expense = models.TextField(db_column='INDIRECT_EXPENSE', blank=True, null=True)  # Field name made lowercase.
    water_gas_expense = models.TextField(db_column='WATER_GAS_EXPENSE', blank=True, null=True)  # Field name made lowercase.
    management_expense = models.TextField(db_column='MANAGEMENT_EXPENSE', blank=True, null=True)  # Field name made lowercase.
    performance_reword = models.TextField(db_column='PERFORMANCE_REWORD', blank=True, null=True)  # Field name made lowercase.
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    region_trial_expense = models.TextField(db_column='REGION_TRIAL_EXPENSE', blank=True, null=True)  # Field name made lowercase.
    other_description = models.TextField(db_column='OTHER_DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    enginerring_expense = models.TextField(db_column='ENGINERRING_EXPENSE', blank=True, null=True)  # Field name made lowercase.
    total_expense = models.TextField(db_column='TOTAL_EXPENSE', blank=True, null=True)  # Field name made lowercase.
    part_type = models.TextField(db_column='PART_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_contract_fund_remark'


class EnvContractMemberInfo(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    contract_id = models.TextField(db_column='CONTRACT_ID')  # Field name made lowercase. This field type is a guess.
    member_name = models.TextField(db_column='MEMBER_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    role = models.TextField(db_column='ROLE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    birth_date = models.TextField(db_column='BIRTH_DATE', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(db_column='TITLE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    country = models.TextField(db_column='COUNTRY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    edu_degree = models.TextField(db_column='EDU_DEGREE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    major = models.TextField(db_column='MAJOR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mobile = models.TextField(db_column='MOBILE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    security_id = models.TextField(db_column='SECURITY_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    signature = models.TextField(db_column='SIGNATURE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    start_date = models.TextField(db_column='START_DATE', blank=True, null=True)  # Field name made lowercase.
    work_desc = models.TextField(db_column='WORK_DESC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    work_volume = models.TextField(db_column='WORK_VOLUME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    main_resume = models.TextField(db_column='MAIN_RESUME', blank=True, null=True)  # Field name made lowercase.
    phone = models.TextField(db_column='PHONE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fax = models.TextField(db_column='FAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    email = models.TextField(db_column='EMAIL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    company_name = models.TextField(db_column='COMPANY_Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    company_title = models.TextField(db_column='COMPANY_TITLE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sequence = models.TextField(db_column='SEQUENCE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    security_type = models.TextField(db_column='SECURITY_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    area_code = models.TextField(db_column='AREA_CODE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_contract_member_info'


class EnvContractSchedule(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    project_id = models.TextField(db_column='PROJECT_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    contract_id = models.TextField(db_column='CONTRACT_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    phase = models.TextField(db_column='PHASE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    start_date = models.TextField(db_column='START_DATE', blank=True, null=True)  # Field name made lowercase.
    end_date = models.TextField(db_column='END_DATE', blank=True, null=True)  # Field name made lowercase.
    content_and_goal = models.TextField(db_column='CONTENT_AND_GOAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    self_raised_fund = models.TextField(db_column='SELF_RAISED_FUND', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    financial_fund = models.TextField(db_column='FINANCIAL_FUND', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    main_use_items = models.TextField(db_column='MAIN_USE_ITEMS', blank=True, null=True)  # Field name made lowercase.
    amount_use = models.TextField(db_column='AMOUNT_USE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_contract_schedule'


class EnvFounderProjectFund(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    project_id = models.TextField(db_column='PROJECT_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sponsor = models.TextField(db_column='SPONSOR')  # Field name made lowercase. This field type is a guess.
    total_expense = models.TextField(db_column='TOTAL_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    organization_expense = models.TextField(db_column='ORGANIZATION_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    propaganda_expense = models.TextField(db_column='PROPAGANDA_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    meeting_expense = models.TextField(db_column='MEETING_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    meeting_field_expense = models.TextField(db_column='MEETING_FIELD_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    meeting_equipment_expense = models.TextField(db_column='MEETING_EQUIPMENT_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    meeting_data_expense = models.TextField(db_column='MEETING_DATA_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    meeting_other_expense = models.TextField(db_column='MEETING_OTHER_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    guest_expense = models.TextField(db_column='GUEST_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    guest_traffic_expense = models.TextField(db_column='GUEST_TRAFFIC_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    guest_accommodation_expense = models.TextField(db_column='GUEST_ACCOMMODATION_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    guest_meals_expense = models.TextField(db_column='GUEST_MEALS_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    guest_other_expense = models.TextField(db_column='GUEST_OTHER_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    safty_and_traffic_security_expense = models.TextField(db_column='SAFTY_AND_TRAFFIC_SECURITY_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    other_expense = models.TextField(db_column='OTHER_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    other_reception_expense = models.TextField(db_column='OTHER_RECEPTION_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    other_staff_expense = models.TextField(db_column='OTHER_STAFF_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    other_other_expense = models.TextField(db_column='OTHER_OTHER_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    other_description = models.TextField(db_column='OTHER_DESCRIPTION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'env_founder_project_fund'


class EnvIncubatorInfo(models.Model):
    project_id = models.TextField(db_column='PROJECT_ID', unique=True)  # Field name made lowercase. This field type is a guess.
    type = models.TextField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    headcount = models.TextField(db_column='HEADCOUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    degrees_number = models.TextField(db_column='DEGREES_NUMBER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    education_proportion = models.TextField(db_column='EDUCATION_PROPORTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    use_area = models.TextField(db_column='USE_AREA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    service_area = models.TextField(db_column='SERVICE_AREA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    service_proportion = models.TextField(db_column='SERVICE_PROPORTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    disposal_site_number = models.TextField(db_column='DISPOSAL_SITE_NUMBER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    patent_number = models.TextField(db_column='PATENT_NUMBER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    patent_proportion = models.TextField(db_column='PATENT_PROPORTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cumulative_number = models.TextField(db_column='CUMULATIVE_NUMBER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    jobs_number = models.TextField(db_column='JOBS_NUMBER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    to_proportion = models.TextField(db_column='TO_PROPORTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    incubation_amount = models.TextField(db_column='INCUBATION_AMOUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    training_proportion = models.TextField(db_column='TRAINING_PROPORTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    summary = models.TextField(db_column='SUMMARY', blank=True, null=True)  # Field name made lowercase.
    service_content = models.TextField(db_column='SERVICE_CONTENT', blank=True, null=True)  # Field name made lowercase.
    development = models.TextField(db_column='DEVELOPMENT', blank=True, null=True)  # Field name made lowercase.
    employment_work = models.TextField(db_column='EMPLOYMENT_WORK', blank=True, null=True)  # Field name made lowercase.
    performance_work = models.TextField(db_column='PERFORMANCE_WORK', blank=True, null=True)  # Field name made lowercase.
    incubator_name = models.TextField(db_column='INCUBATOR_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_incubator_info'


class EnvInvitationSystemMapping(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    item_id = models.TextField(db_column='ITEM_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    guide = models.TextField(db_column='GUIDE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    contact_person = models.TextField(db_column='CONTACT_PERSON', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    contact_mobile = models.TextField(db_column='CONTACT_MOBILE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    contact_email = models.TextField(db_column='CONTACT_EMAIL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_invitation_system_mapping'


class EnvPecialdays(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    start_end = models.TextField(db_column='START_END')  # Field name made lowercase.
    end_end = models.TextField(db_column='END_END')  # Field name made lowercase.
    type = models.TextField(db_column='TYPE')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_pecialdays'


class EnvProjectAccessoryInfo(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    project_id = models.TextField(db_column='PROJECT_ID')  # Field name made lowercase. This field type is a guess.
    type = models.TextField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    file_id = models.TextField(db_column='FILE_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sequence = models.TextField(db_column='SEQUENCE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_project_accessory_info'


class EnvProjectAccountFirmInfo(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    application_type = models.TextField(db_column='APPLICATION_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    certificate_number = models.TextField(db_column='CERTIFICATE_NUMBER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    declare_batch = models.TextField(db_column='DECLARE_BATCH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    high_tech_field = models.TextField(db_column='HIGH_TECH_FIELD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sub_high_tech_field = models.TextField(db_column='SUB_HIGH_TECH_FIELD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    account_firm_recent_year = models.TextField(db_column='ACCOUNT_FIRM_RECENT_YEAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cpa_name_recent_year = models.TextField(db_column='CPA_NAME_RECENT_YEAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    account_firm_recent_3year = models.TextField(db_column='ACCOUNT_FIRM_RECENT_3YEAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    file_id = models.TextField(db_column='FILE_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    is_different = models.TextField(db_column='IS_DIFFERENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    project_id = models.TextField(db_column='PROJECT_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cpa_name_recent_3year = models.TextField(db_column='CPA_NAME_RECENT_3YEAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cpa_name_last_year = models.TextField(db_column='CPA_NAME_LAST_YEAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cpa_name_prelast_year = models.TextField(db_column='CPA_NAME_PRELAST_YEAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cpa_name_bef_prelast_year = models.TextField(db_column='CPA_NAME_BEF_PRELAST_YEAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    account_firm_last_year = models.TextField(db_column='ACCOUNT_FIRM_LAST_YEAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    account_firm_prelast_year = models.TextField(db_column='ACCOUNT_FIRM_PRELAST_YEAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    account_firm_bef_prelast_year = models.TextField(db_column='ACCOUNT_FIRM_BEF_PRELAST_YEAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_project_account_firm_info'


class EnvProjectAccountingInformation(models.Model):
    project_id = models.TextField(db_column='PROJECT_ID', unique=True)  # Field name made lowercase. This field type is a guess.
    contact_unit = models.TextField(db_column='CONTACT_UNIT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    contact_plane = models.TextField(db_column='CONTACT_PLANE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    email = models.TextField(db_column='EMAIL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mobile = models.TextField(db_column='MOBILE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    address = models.TextField(db_column='ADDRESS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fax = models.TextField(db_column='FAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    postcode = models.TextField(db_column='POSTCODE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    document_type = models.TextField(db_column='DOCUMENT_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    identification_number = models.TextField(db_column='IDENTIFICATION_NUMBER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    income_office = models.TextField(db_column='INCOME_OFFICE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    income_accountant = models.TextField(db_column='INCOME_ACCOUNTANT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    research_office = models.TextField(db_column='RESEARCH_OFFICE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    research_accountant = models.TextField(db_column='RESEARCH_ACCOUNTANT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fourteen_office = models.TextField(db_column='FOURTEEN_OFFICE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fourteen_accountant = models.TextField(db_column='FOURTEEN_ACCOUNTANT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    thirteen_office = models.TextField(db_column='THIRTEEN_OFFICE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    thirteen_accountant = models.TextField(db_column='THIRTEEN_ACCOUNTANT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    twelve_office = models.TextField(db_column='TWELVE_OFFICE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    twelve_accountant = models.TextField(db_column='TWELVE_ACCOUNTANT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    difference = models.TextField(db_column='DIFFERENCE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    difference_explain = models.TextField(db_column='DIFFERENCE_EXPLAIN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_project_accounting_information'


class EnvProjectAchievement(models.Model):
    project_id = models.TextField(db_column='PROJECT_ID', unique=True)  # Field name made lowercase. This field type is a guess.
    paper_count = models.TextField(db_column='PAPER_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    article_count = models.TextField(db_column='ARTICLE_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    patent_count = models.TextField(db_column='PATENT_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    trained_post_doctoral_count = models.TextField(db_column='TRAINED_POST_DOCTORAL_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    trained_doctor_count = models.TextField(db_column='TRAINED_DOCTOR_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    trained_master_count = models.TextField(db_column='TRAINED_MASTER_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hold_meeting_count = models.TextField(db_column='HOLD_MEETING_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_project_achievement'


class EnvProjectActivityInfo(models.Model):
    id = models.TextField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    project_id = models.TextField(db_column='PROJECT_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    activity_name = models.TextField(db_column='ACTIVITY_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    organizer_num = models.TextField(db_column='ORGANIZER_NUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    attendance = models.TextField(db_column='ATTENDANCE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    foreign_num = models.TextField(db_column='FOREIGN_NUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    activity_address = models.TextField(db_column='ACTIVITY_ADDRESS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    activity_time = models.TextField(db_column='ACTIVITY_TIME', blank=True, null=True)  # Field name made lowercase.
    organizer = models.TextField(db_column='ORGANIZER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    co_organizer = models.TextField(db_column='CO_ORGANIZER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    undertake_unit = models.TextField(db_column='UNDERTAKE_UNIT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    support_unit = models.TextField(db_column='SUPPORT_UNIT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    activity_basis = models.TextField(db_column='ACTIVITY_BASIS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    approve_unit = models.TextField(db_column='APPROVE_UNIT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    participater1 = models.TextField(db_column='PARTICIPATER1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    participater2 = models.TextField(db_column='PARTICIPATER2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    participater3 = models.TextField(db_column='PARTICIPATER3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    participater4 = models.TextField(db_column='PARTICIPATER4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    participater5 = models.TextField(db_column='PARTICIPATER5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    participater6 = models.TextField(db_column='PARTICIPATER6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    participater7 = models.TextField(db_column='PARTICIPATER7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    participater8 = models.TextField(db_column='PARTICIPATER8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    participater9 = models.TextField(db_column='PARTICIPATER9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    participater10 = models.TextField(db_column='PARTICIPATER10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    participater12 = models.TextField(db_column='PARTICIPATER12', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    participater13 = models.TextField(db_column='PARTICIPATER13', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    participater14 = models.TextField(db_column='PARTICIPATER14', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    participater15 = models.TextField(db_column='PARTICIPATER15', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    participater16 = models.TextField(db_column='PARTICIPATER16', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    participater17 = models.TextField(db_column='PARTICIPATER17', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    participater18 = models.TextField(db_column='PARTICIPATER18', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    participater11 = models.TextField(db_column='PARTICIPATER11', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'env_project_activity_info'


class ZfjcCompanyBaseInfoRegionDist(models.Model):
    id = models.TextField(db_column='myID', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    region = models.TextField(db_column='REGION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    industry_type = models.TextField(db_column='INDUSTRY_TYPE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    year = models.TextField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    company_num = models.TextField(db_column='COMPANY_NUM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    register_capital = models.TextField(db_column='REGISTER_CAPITAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    research_office_space = models.TextField(db_column='RESEARCH_OFFICE_SPACE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    factory_space = models.TextField(db_column='FACTORY_SPACE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    offshore_sales_unit_count = models.TextField(db_column='OFFSHORE_SALES_UNIT_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    offshore_resarch_unit_count = models.TextField(db_column='OFFSHORE_RESARCH_UNIT_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    year_power_consumption = models.TextField(db_column='YEAR_POWER_CONSUMPTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    year_water_consumption = models.TextField(db_column='YEAR_WATER_CONSUMPTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_eployee_count = models.TextField(db_column='TOTAL_EPLOYEE_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    returned_student_count = models.TextField(db_column='RETURNED_STUDENT_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    foreign_expert_count = models.TextField(db_column='FOREIGN_EXPERT_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    graduate_count = models.TextField(db_column='GRADUATE_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hr_eployee_count = models.TextField(db_column='HR_EPLOYEE_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sales_eployee_count = models.TextField(db_column='SALES_EPLOYEE_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rd_eployee_count = models.TextField(db_column='RD_EPLOYEE_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    manufacture_eployee_count = models.TextField(db_column='MANUFACTURE_EPLOYEE_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    other_job_count = models.TextField(db_column='OTHER_JOB_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    doctor_eployee_count = models.TextField(db_column='DOCTOR_EPLOYEE_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    master_eployee_count = models.TextField(db_column='MASTER_EPLOYEE_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    undergraduate_eployee_count = models.TextField(db_column='UNDERGRADUATE_EPLOYEE_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    junior_college_eployee_count = models.TextField(db_column='JUNIOR_COLLEGE_EPLOYEE_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    otehr_degree_eployee_count = models.TextField(db_column='OTEHR_DEGREE_EPLOYEE_COUNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sinior_eployee_professor = models.TextField(db_column='SINIOR_EPLOYEE_PROFESSOR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    midium_eployee_professor = models.TextField(db_column='MIDIUM_EPLOYEE_PROFESSOR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    junior_eployee_professor = models.TextField(db_column='JUNIOR_EPLOYEE_PROFESSOR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    other_title_eployee_professor = models.TextField(db_column='OTHER_TITLE_EPLOYEE_PROFESSOR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_net_cashflow = models.TextField(db_column='TOTAL_NET_CASHFLOW', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    operation_net_cashflow = models.TextField(db_column='OPERATION_NET_CASHFLOW', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sales_income = models.TextField(db_column='SALES_INCOME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    promotion_expense = models.TextField(db_column='PROMOTION_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    governmnet_loan = models.TextField(db_column='GOVERNMNET_LOAN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    matured_governmnet_loan = models.TextField(db_column='MATURED_GOVERNMNET_LOAN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_income = models.TextField(db_column='TOTAL_INCOME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    high_tech_product_income = models.TextField(db_column='HIGH_TECH_PRODUCT_INCOME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    software_product_income = models.TextField(db_column='SOFTWARE_PRODUCT_INCOME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_industrial_value = models.TextField(db_column='TOTAL_INDUSTRIAL_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    high_tech_product_value = models.TextField(db_column='HIGH_TECH_PRODUCT_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pro_int_right_value = models.TextField(db_column='PRO_INT_RIGHT_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_increase_value = models.TextField(db_column='TOTAL_INCREASE_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dep_fix_assets_value = models.TextField(db_column='DEP_FIX_ASSETS_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    manufacture_net_tax = models.TextField(db_column='MANUFACTURE_NET_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    operation_net_value = models.TextField(db_column='OPERATION_NET_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_export_value = models.TextField(db_column='TOTAL_EXPORT_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    high_tech_export_value = models.TextField(db_column='HIGH_TECH_EXPORT_VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    net_margin = models.TextField(db_column='NET_MARGIN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_tax = models.TextField(db_column='TOTAL_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    value_added_tax = models.TextField(db_column='VALUE_ADDED_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    operation_tax = models.TextField(db_column='OPERATION_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    income_tax = models.TextField(db_column='INCOME_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    personal_income_tax = models.TextField(db_column='PERSONAL_INCOME_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_relief_tax = models.TextField(db_column='TOTAL_RELIEF_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    relief_value_added_tax = models.TextField(db_column='RELIEF_VALUE_ADDED_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    relief_operation_tax = models.TextField(db_column='RELIEF_OPERATION_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    relief_income_tax = models.TextField(db_column='RELIEF_INCOME_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    relief_jjkc_tax = models.TextField(db_column='RELIEF_JJKC_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    relief_high_tech_pro_tax = models.TextField(db_column='RELIEF_HIGH_TECH_PRO_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_assets = models.TextField(db_column='TOTAL_ASSETS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_liability = models.TextField(db_column='TOTAL_LIABILITY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_fixed_assets = models.TextField(db_column='TOTAL_FIXED_ASSETS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fixed_assets_investment = models.TextField(db_column='FIXED_ASSETS_INVESTMENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rd_expense = models.TextField(db_column='RD_EXPENSE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    financial_appropriation = models.TextField(db_column='FINANCIAL_APPROPRIATION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    operation_income = models.TextField(db_column='OPERATION_INCOME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tech_act_income = models.TextField(db_column='TECH_ACT_INCOME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    high_tech_product_service_income = models.TextField(db_column='HIGH_TECH_PRODUCT_SERVICE_INCOME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    major_support_income_tax_relief = models.TextField(db_column='MAJOR_SUPPORT_INCOME_TAX_RELIEF', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tech_transport_income_tax_relief = models.TextField(db_column='TECH_TRANSPORT_INCOME_TAX_RELIEF', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    company_income_tax = models.TextField(db_column='COMPANY_INCOME_TAX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    app_patent = models.TextField(db_column='APP_PATENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    app_pra_patent = models.TextField(db_column='APP_PRA_PATENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    app_sur_patent = models.TextField(db_column='APP_SUR_PATENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    own_patent = models.TextField(db_column='OWN_PATENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    own_pra_patent = models.TextField(db_column='OWN_PRA_PATENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    own_sur_patent = models.TextField(db_column='OWN_SUR_PATENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pub_paper = models.TextField(db_column='PUB_PAPER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pub_tech_paper = models.TextField(db_column='PUB_TECH_PAPER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    own_software = models.TextField(db_column='OWN_SOFTWARE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    own_ic_layout = models.TextField(db_column='OWN_IC_LAYOUT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    own_brand = models.TextField(db_column='OWN_BRAND', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    int_tech_stan = models.TextField(db_column='INT_TECH_STAN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nat_high_tech_reward = models.TextField(db_column='NAT_HIGH_TECH_REWARD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nat_key_lab = models.TextField(db_column='NAT_KEY_LAB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nat_engineering_center = models.TextField(db_column='NAT_ENGINEERING_CENTER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nat_project = models.TextField(db_column='NAT_PROJECT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nat_tech_stan = models.TextField(db_column='NAT_TECH_STAN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ind_tech_stan = models.TextField(db_column='IND_TECH_STAN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pro_high_tech_reward = models.TextField(db_column='PRO_HIGH_TECH_REWARD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pro_key_lab = models.TextField(db_column='PRO_KEY_LAB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mun_key_lab = models.TextField(db_column='MUN_KEY_LAB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pro_engineering_center = models.TextField(db_column='PRO_ENGINEERING_CENTER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mun_engineering_center = models.TextField(db_column='MUN_ENGINEERING_CENTER', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mun_project = models.TextField(db_column='MUN_PROJECT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    authorised_software = models.TextField(db_column='AUTHORISED_SOFTWARE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'zfjc_company_base_info_region_dist'