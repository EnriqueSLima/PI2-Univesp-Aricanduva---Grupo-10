# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
# *** Modelos gerados diretamente do bancos de dados criado. ***

# *** Para registrar alunos.
class Cliente(models.Model):
    id_cliente = models.AutoField(db_column='Id_cliente', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nome_social = models.CharField(max_length=40, blank=True, null=True)
    tipo = models.CharField(max_length=25, blank=True, null=True)
    cpf = models.CharField(max_length=18, blank=True, null=True)
    ie_rg = models.CharField(max_length=25, blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    contato = models.CharField(max_length=50, blank=True, null=True)
    ddd = models.CharField(max_length=2, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)  # This field type is a guess.
    ativo = models.BooleanField(blank=True, null=True)
    ra = models.CharField(max_length=5, blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'
    
    def __str__(self):
        return self.nome.strip()

# *** Para registrar editoras.
class Editora(models.Model):
    id_editora = models.AutoField(db_column='Id_Editora', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=40, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    contato = models.CharField(max_length=50, blank=True, null=True)
    ddd = models.CharField(max_length=2, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_usuario = models.IntegerField(blank=True, null=True)
    ult_alteracao = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Editora'
    
    def __str__(self):
            return self.nome.strip()

# *** Para registrar livros.
class Produtos(models.Model):
    id_produto = models.AutoField(primary_key=True)
    tombo = models.DateTimeField(blank=True, null=True)
    numero_tombo = models.CharField(max_length=20, blank=True, null=True)
    codigo_de_barras = models.CharField(max_length=13, blank=True, null=True)
    autor = models.CharField(db_column='Autor', max_length=120, blank=True, null=True)  # Field name made lowercase.
    titulo = models.CharField(max_length=120, blank=True, null=True)
    procedencia = models.CharField(db_column='Procedencia', max_length=120, blank=True, null=True)  # Field name made lowercase.
    estoque = models.IntegerField(blank=True, null=True)
    local_estoque = models.CharField(max_length=30, blank=True, null=True)
    id_editora = models.IntegerField(db_column='id_Editora', blank=True, null=True)  # Field name made lowercase.
    colecao = models.CharField(max_length=120, blank=True, null=True)
    edicao = models.CharField(max_length=20, blank=True, null=True)
    volume = models.CharField(db_column='Volume', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ano = models.CharField(max_length=4, blank=True, null=True)
    id_tipo_produto = models.IntegerField(blank=True, null=True)
    defeito = models.BooleanField(blank=True, null=True)
    bloquear = models.BooleanField(blank=True, null=True)
    aquisicao_c = models.BooleanField(db_column='Aquisicao_c', blank=True, null=True)  # Field name made lowercase.
    aquisicao_d = models.BooleanField(db_column='Aquisicao_d', blank=True, null=True)  # Field name made lowercase.
    aquisicao_t = models.BooleanField(db_column='Aquisicao_t', blank=True, null=True)  # Field name made lowercase.
    id_usuario = models.IntegerField(blank=True, null=True)
    ult_alteracao = models.DateTimeField(blank=True, null=True)
    obs = models.TextField(blank=True, null=True)  # This field type is a guess.
    data_cadastro = models.DateTimeField(blank=True, null=True)
    #capa = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produtos'
    
    def __str__(self):
        return self.titulo.strip()

# *** Para registrar categorías de livros.
class TipoProduto(models.Model):
    id_tipo_produto = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=30, blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_produto'

        def __str__(self):
            return self.descricao.strip()

# *** Para registrar possíveis usuários do sistema.
class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    senha = models.CharField(max_length=10)
    id_unidade = models.IntegerField()
    id_acesso = models.IntegerField()
    ativo = models.BooleanField(blank=True, null=True)
    obs = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'usuarios'

    def __str__(self):
            return self.nome.strip()

# *** Para registrar empréstimos.
class Locacao(models.Model):
    id_locacao = models.IntegerField(primary_key=True, default=0)
    #id_cliente = models.IntegerField(blank=True, null=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    emissao = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    observacao = models.CharField(max_length=200, blank=True, null=True)
    id_usuario = models.IntegerField(blank=True, null=True)
    reserva = models.BooleanField(db_column='Reserva', blank=True, null=True)  # Field name made lowercase.
    confirma = models.BooleanField(db_column='Confirma', blank=True, null=True)  # Field name made lowercase.
    liquida = models.BooleanField(db_column='Liquida', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Locacao'

# *** Para registrar ????
class LocacaoItens(models.Model):
    id_locaitens = models.IntegerField(blank=True, null=True)
    id_locacao = models.IntegerField(blank=True, null=True, default=0)
    #id_produto = models.IntegerField(blank=True, null=True)
    id_produto = models.ForeignKey(Produtos, models.DO_NOTHING, db_column='id_produto', blank=True, null=True)
    titulo = models.CharField(max_length=250, blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)
    dev_prevista_ori = models.DateTimeField(blank=True, null=True)
    renovou = models.IntegerField(blank=True, null=True)
    dev_prevista = models.DateTimeField(blank=True, null=True)
    dev_realizada = models.DateTimeField(blank=True, null=True)
    devolvido = models.BooleanField(blank=True, null=True)
    id_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Locacao_itens'

# *** Para registrar acessos e interações.
class Kardex(models.Model):
    data = models.DateTimeField()
    quantidade = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    saldo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    unidade = models.CharField(max_length=2, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_operacao = models.IntegerField(blank=True, null=True)
    id_destinatario = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_destinatario', blank=True, null=True)
    destinatario = models.CharField(db_column='Destinatario', max_length=40, blank=True, null=True)  # Field name made lowercase.
    id_usuario = models.IntegerField(blank=True, null=True)
    id_unidade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kardex'

class KardexOperacao(models.Model):
    id_operacao = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50, blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)
    entrada = models.BooleanField(blank=True, null=True)
    saida = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kardex_operacao'

class Acessos(models.Model):
    id_acesso = models.AutoField(primary_key=True)
    acesso = models.CharField(max_length=50, blank=True, null=True)
    id_usuario = models.IntegerField(blank=True, null=True)
    id_unidade = models.IntegerField()
    master = models.BooleanField(blank=True, null=True)
    incluir = models.BooleanField(blank=True, null=True)
    alterar = models.BooleanField(blank=True, null=True)
    imprimir = models.BooleanField(blank=True, null=True)
    excluir = models.BooleanField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'acessos'

# *** Modelos gerados pelos módulos de autenticação do Django. ***
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)

class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)

class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

# *** Modelos gerados pelos módulos de administração do Django. ***
class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)

# *** Modelos gerados pelos módulos de migração do Django. ***
class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

# *** Modelos gerados pelos módulos de sessão do Django. ***
class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
