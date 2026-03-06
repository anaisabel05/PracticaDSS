# Instrucciones de Escritura de Código Python

## Prioridades

Este documento establece las directrices para escribir código Python en este proyecto, con enfoque en **legibilidad** y **optimización**.

---

## 1. Legibilidad

### 1.1 Nombres Descriptivos
- Usar nombres claros y explícitos para variables, funciones y clases
- Evitar abreviaturas confusas
- Preferir claridad sobre brevedad

```python
# ❌ Malo
def val_dni(d):
    return d.isalnum()

# ✅ Bueno
def validar_dni(dni):
    return dni.isalnum()
```

### 1.2 Comentarios y Docstrings
- Incluir docstrings en todas las funciones y clases
- Usar comentarios para explicar por qué, no qué
- Seguir el formato Google o NumPy

```python
def validar_dni(dni):
    """
    Valida un DNI español con formato 8 dígitos + 1 letra.
    
    Args:
        dni (str): El DNI a validar
    
    Returns:
        bool: True si es válido, False en caso contrario
    """
    pass
```

### 1.3 Formato y Estilo
- Seguir PEP 8
- Máximo 79 caracteres por línea (88 con Black)
- 4 espacios de indentación
- Usar linters: `pylint`, `flake8`, `black`

### 1.4 Estructura del Código
- Una función = una responsabilidad (SRP)
- Mantener funciones cortas y enfocadas (máx. 20 líneas)
- Agrupar funciones relacionadas en clases

---

## 2. Optimización

### 2.1 Complejidad Temporal
- Analizar la complejidad Big O
- Evitar loops anidados innecesarios
- Usar estructuras de datos eficientes (sets, dicts vs listas)

```python
# ❌ O(n²) - Ineficiente
def buscar_duplicados(lista):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] == lista[j]:
                return True

# ✅ O(n) - Óptimo
def buscar_duplicados(lista):
    return len(lista) != len(set(lista))
```

### 2.2 Complejidad Espacial
- Minimizar uso de memoria
- Evitar copias innecesarias
- Usar generadores para datos grandes

```python
# ❌ Alto consumo de memoria
def procesar_numeros(n):
    numeros = [i**2 for i in range(n)]
    return sum(numeros)

# ✅ Eficiente
def procesar_numeros(n):
    return sum(i**2 for i in range(n))
```

### 2.3 Operaciones de I/O
- Leer archivos en chunks si son grandes
- Usar context managers (`with`)
- Minimizar llamadas a base de datos

### 2.4 Librerías Eficientes
- Usar `NumPy` para operaciones matemáticas
- Usar `Pandas` para análisis de datos
- Evitar reinventar la rueda

---

## 3. Testing

- Escribir tests unitarios para funciones críticas
- Usar `pytest` o `unittest`
- Mantener cobertura > 70%

```python
import unittest

class TestValidarDNI(unittest.TestCase):
    def test_dni_valido(self):
        self.assertTrue(validar_dni("12345678Z"))
    
    def test_dni_invalido(self):
        self.assertFalse(validar_dni("12345678A"))
```

---

## 4. Control de Versiones

- Commits con mensajes claros y descriptivos
- Una feature por rama
- Review de código antes de merge

---

## 5. Checklist Antes de Commit

- [ ] Código sigue PEP 8
- [ ] Funciones tienen docstrings
- [ ] Tests pasan correctamente
- [ ] No hay código duplicado
- [ ] Complejidad aceptable
- [ ] Sin warnings de linters

---

## Herramientas Recomendadas

| Herramienta | Propósito |
|---|---|
| `black` | Formateador automático |
| `pylint` | Análisis estático |
| `flake8` | Linter |
| `pytest` | Testing |
| `mypy` | Type checking |

---

**Última actualización:** 6 de marzo de 2026
