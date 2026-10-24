-- Esquema inicial para estudo; compatível com a sintaxe básica do SQLite.
-- Use apenas dados fictícios nos exercícios.

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    identificador TEXT NOT NULL UNIQUE,
    ativo INTEGER NOT NULL DEFAULT 1 CHECK (ativo IN (0, 1))
);

CREATE TABLE IF NOT EXISTS marcacoes_ponto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    funcionario_id INTEGER NOT NULL,
    tipo TEXT NOT NULL CHECK (tipo IN ('entrada', 'inicio_intervalo', 'fim_intervalo', 'saida')),
    registrado_em TEXT NOT NULL,
    observacao TEXT,
    FOREIGN KEY (funcionario_id) REFERENCES funcionarios(id)
);

CREATE INDEX IF NOT EXISTS idx_marcacoes_funcionario_data
ON marcacoes_ponto (funcionario_id, registrado_em);

-- Próximas etapas: definir regras para turnos noturnos, marcações duplicadas,
-- correções auditáveis e cálculos de horas antes de gerar relatórios.
