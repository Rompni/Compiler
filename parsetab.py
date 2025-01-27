
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocPRINTleftPLUSMINUSleftTIMESDIVIDEleftLPARENRPARENrightUMINUSAND CHARACTER COLON COMMA DIVIDE ELSE END EQ EQUAL FALSE FLOAT FOR GE GT ID IDTYPE IF INIT INTEGER LAND LBRACE LBRACKET LE LNOT LOR LPAREN LSHIFT LT MINUS MODULO NE NOT OR PERIOD PLUS PRINT RBRACE RBRACKET RPAREN RSHIFT SEMI STRING TIMES TRUE WHILE XORstart : INIT bodybody : LBRACE all_sentences RBRACEall_sentences : all_sentences list_sentences\n                    | sentencelist_sentences : sentencesentence : declaration\n                | assign\n                | sentence_while\n                | sentence_for\n                | sentence_if\n                | print\n                | emptyexpression : expression PLUS expression\n                    | expression MINUS expression\n                    | expression TIMES expression\n                    | expression DIVIDE expressionexpression : MINUS expression %prec UMINUSexpression : LPAREN expression RPARENexpression : INTEGER\n                 | FLOATexpression : IDsentence_while : WHILE LPAREN condition RPAREN bodysentence_for : FOR LPAREN assign condition SEMI assign RPAREN bodysentence_if : IF LPAREN condition RPAREN body\n                  | IF LPAREN condition RPAREN body ELSE LPAREN RPAREN bodyconditions : LOR\n                  | LAND\n                  | LNOT\n                  | LT\n                  | GT\n                  | LE\n                  | GE\n                  | EQ\n                  | NEcondition : expression conditions expression\n                    expression : conditiondeclaration : IDTYPE ID SEMIboolean : TRUE\n                | FALSEtvariable : STRING\n                 | CHARACTER\n                 | boolean\n                 print : PRINT tvariable SEMI\n            |  PRINT expression SEMIassign : IDTYPE ID EQUAL tvariable SEMI\n                | IDTYPE ID EQUAL expression SEMI\n                assign : ID EQUAL tvariable SEMI\n             | ID EQUAL expression SEMI\n             empty : '
    
_lr_action_items = {'INIT':([0,],[2,]),'$end':([1,3,20,],[0,-1,-2,]),'LBRACE':([2,72,75,89,92,],[4,4,4,4,4,]),'IDTYPE':([4,5,6,7,8,9,10,11,12,13,20,21,22,26,41,50,51,70,71,82,83,84,85,86,91,93,],[14,14,-4,-6,-7,-8,-9,-10,-11,-12,-2,-3,-5,48,-37,-43,-44,-47,-48,-45,-46,-22,48,-24,-23,-25,]),'ID':([4,5,6,7,8,9,10,11,12,13,14,19,20,21,22,24,25,26,27,33,34,41,42,47,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,82,83,84,85,86,91,93,],[15,15,-4,-6,-7,-8,-9,-10,-11,-12,23,37,-2,-3,-5,37,37,15,37,37,37,-37,37,37,74,-43,-44,37,37,37,37,37,-26,-27,-28,-29,-30,-31,-32,-33,-34,-47,-48,-45,-46,-22,15,-24,-23,-25,]),'WHILE':([4,5,6,7,8,9,10,11,12,13,20,21,22,41,50,51,70,71,82,83,84,86,91,93,],[16,16,-4,-6,-7,-8,-9,-10,-11,-12,-2,-3,-5,-37,-43,-44,-47,-48,-45,-46,-22,-24,-23,-25,]),'FOR':([4,5,6,7,8,9,10,11,12,13,20,21,22,41,50,51,70,71,82,83,84,86,91,93,],[17,17,-4,-6,-7,-8,-9,-10,-11,-12,-2,-3,-5,-37,-43,-44,-47,-48,-45,-46,-22,-24,-23,-25,]),'IF':([4,5,6,7,8,9,10,11,12,13,20,21,22,41,50,51,70,71,82,83,84,86,91,93,],[18,18,-4,-6,-7,-8,-9,-10,-11,-12,-2,-3,-5,-37,-43,-44,-47,-48,-45,-46,-22,-24,-23,-25,]),'PRINT':([4,5,6,7,8,9,10,11,12,13,20,21,22,41,50,51,70,71,82,83,84,86,91,93,],[19,19,-4,-6,-7,-8,-9,-10,-11,-12,-2,-3,-5,-37,-43,-44,-47,-48,-45,-46,-22,-24,-23,-25,]),'RBRACE':([4,5,6,7,8,9,10,11,12,13,20,21,22,41,50,51,70,71,82,83,84,86,91,93,],[-49,20,-4,-6,-7,-8,-9,-10,-11,-12,-2,-3,-5,-37,-43,-44,-47,-48,-45,-46,-22,-24,-23,-25,]),'EQUAL':([15,23,74,],[24,42,42,]),'LPAREN':([16,17,18,19,24,25,27,33,34,42,47,52,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,82,83,88,],[25,26,27,34,34,34,34,34,34,34,34,34,34,34,34,34,-26,-27,-28,-29,-30,-31,-32,-33,-34,-47,-48,-45,-46,90,]),'STRING':([19,24,42,],[30,30,30,]),'CHARACTER':([19,24,42,],[31,31,31,]),'MINUS':([19,24,25,27,29,33,34,35,36,37,38,42,44,45,46,47,49,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,73,76,77,78,79,80,81,82,83,],[33,33,33,33,53,33,33,-19,-20,-21,-36,33,53,-36,53,33,-36,33,33,33,33,33,-26,-27,-28,-29,-30,-31,-32,-33,-34,-17,53,53,-47,-48,-36,-13,-14,-15,-16,53,-18,-45,-46,]),'INTEGER':([19,24,25,27,33,34,42,47,52,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,82,83,],[35,35,35,35,35,35,35,35,35,35,35,35,35,-26,-27,-28,-29,-30,-31,-32,-33,-34,-47,-48,-45,-46,]),'FLOAT':([19,24,25,27,33,34,42,47,52,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,82,83,],[36,36,36,36,36,36,36,36,36,36,36,36,36,-26,-27,-28,-29,-30,-31,-32,-33,-34,-47,-48,-45,-46,]),'TRUE':([19,24,42,],[39,39,39,]),'FALSE':([19,24,42,],[40,40,40,]),'ELSE':([20,86,],[-2,88,]),'SEMI':([23,28,29,30,31,32,35,36,37,38,39,40,43,44,66,68,69,73,76,77,78,79,80,81,],[41,50,51,-40,-41,-42,-19,-20,-21,-36,-38,-39,70,71,-17,82,83,85,-13,-14,-15,-16,-35,-18,]),'PLUS':([29,35,36,37,38,44,45,46,49,66,67,69,73,76,77,78,79,80,81,],[52,-19,-20,-21,-36,52,-36,52,-36,-17,52,52,-36,-13,-14,-15,-16,52,-18,]),'TIMES':([29,35,36,37,38,44,45,46,49,66,67,69,73,76,77,78,79,80,81,],[54,-19,-20,-21,-36,54,-36,54,-36,-17,54,54,-36,54,54,-15,-16,54,-18,]),'DIVIDE':([29,35,36,37,38,44,45,46,49,66,67,69,73,76,77,78,79,80,81,],[55,-19,-20,-21,-36,55,-36,55,-36,-17,55,55,-36,55,55,-15,-16,55,-18,]),'LOR':([29,35,36,37,38,44,45,46,49,66,67,69,73,76,77,78,79,80,81,],[57,-19,-20,-21,-36,57,-36,57,-36,-17,57,57,-36,-13,-14,-15,-16,57,-18,]),'LAND':([29,35,36,37,38,44,45,46,49,66,67,69,73,76,77,78,79,80,81,],[58,-19,-20,-21,-36,58,-36,58,-36,-17,58,58,-36,-13,-14,-15,-16,58,-18,]),'LNOT':([29,35,36,37,38,44,45,46,49,66,67,69,73,76,77,78,79,80,81,],[59,-19,-20,-21,-36,59,-36,59,-36,-17,59,59,-36,-13,-14,-15,-16,59,-18,]),'LT':([29,35,36,37,38,44,45,46,49,66,67,69,73,76,77,78,79,80,81,],[60,-19,-20,-21,-36,60,-36,60,-36,-17,60,60,-36,-13,-14,-15,-16,60,-18,]),'GT':([29,35,36,37,38,44,45,46,49,66,67,69,73,76,77,78,79,80,81,],[61,-19,-20,-21,-36,61,-36,61,-36,-17,61,61,-36,-13,-14,-15,-16,61,-18,]),'LE':([29,35,36,37,38,44,45,46,49,66,67,69,73,76,77,78,79,80,81,],[62,-19,-20,-21,-36,62,-36,62,-36,-17,62,62,-36,-13,-14,-15,-16,62,-18,]),'GE':([29,35,36,37,38,44,45,46,49,66,67,69,73,76,77,78,79,80,81,],[63,-19,-20,-21,-36,63,-36,63,-36,-17,63,63,-36,-13,-14,-15,-16,63,-18,]),'EQ':([29,35,36,37,38,44,45,46,49,66,67,69,73,76,77,78,79,80,81,],[64,-19,-20,-21,-36,64,-36,64,-36,-17,64,64,-36,-13,-14,-15,-16,64,-18,]),'NE':([29,35,36,37,38,44,45,46,49,66,67,69,73,76,77,78,79,80,81,],[65,-19,-20,-21,-36,65,-36,65,-36,-17,65,65,-36,-13,-14,-15,-16,65,-18,]),'RPAREN':([35,36,37,38,45,49,66,67,70,71,76,77,78,79,80,81,82,83,87,90,],[-19,-20,-21,-36,72,75,-17,81,-47,-48,-13,-14,-15,-16,-35,-18,-45,-46,89,92,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'body':([2,72,75,89,92,],[3,84,86,91,93,]),'all_sentences':([4,],[5,]),'sentence':([4,5,],[6,22,]),'declaration':([4,5,],[7,7,]),'assign':([4,5,26,85,],[8,8,47,87,]),'sentence_while':([4,5,],[9,9,]),'sentence_for':([4,5,],[10,10,]),'sentence_if':([4,5,],[11,11,]),'print':([4,5,],[12,12,]),'empty':([4,5,],[13,13,]),'list_sentences':([5,],[21,]),'tvariable':([19,24,42,],[28,43,68,]),'expression':([19,24,25,27,33,34,42,47,52,53,54,55,56,],[29,44,46,46,66,67,69,46,76,77,78,79,80,]),'boolean':([19,24,42,],[32,32,32,]),'condition':([19,24,25,27,33,34,42,47,52,53,54,55,56,],[38,38,45,49,38,38,38,73,38,38,38,38,38,]),'conditions':([29,44,46,66,67,69,76,77,78,79,80,],[56,56,56,56,56,56,56,56,56,56,56,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> INIT body','start',2,'p_start','Rparser.py',22),
  ('body -> LBRACE all_sentences RBRACE','body',3,'p_body','Rparser.py',26),
  ('all_sentences -> all_sentences list_sentences','all_sentences',2,'p_all_sentences','Rparser.py',30),
  ('all_sentences -> sentence','all_sentences',1,'p_all_sentences','Rparser.py',31),
  ('list_sentences -> sentence','list_sentences',1,'p_list_sentences','Rparser.py',35),
  ('sentence -> declaration','sentence',1,'p_sentence','Rparser.py',39),
  ('sentence -> assign','sentence',1,'p_sentence','Rparser.py',40),
  ('sentence -> sentence_while','sentence',1,'p_sentence','Rparser.py',41),
  ('sentence -> sentence_for','sentence',1,'p_sentence','Rparser.py',42),
  ('sentence -> sentence_if','sentence',1,'p_sentence','Rparser.py',43),
  ('sentence -> print','sentence',1,'p_sentence','Rparser.py',44),
  ('sentence -> empty','sentence',1,'p_sentence','Rparser.py',45),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','Rparser.py',49),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','Rparser.py',50),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','Rparser.py',51),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','Rparser.py',52),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','Rparser.py',65),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','Rparser.py',70),
  ('expression -> INTEGER','expression',1,'p_expression_number','Rparser.py',75),
  ('expression -> FLOAT','expression',1,'p_expression_number','Rparser.py',76),
  ('expression -> ID','expression',1,'p_expression_id','Rparser.py',81),
  ('sentence_while -> WHILE LPAREN condition RPAREN body','sentence_while',5,'p_sentence_while','Rparser.py',92),
  ('sentence_for -> FOR LPAREN assign condition SEMI assign RPAREN body','sentence_for',8,'p_sentence_for','Rparser.py',96),
  ('sentence_if -> IF LPAREN condition RPAREN body','sentence_if',5,'p_sentence_if','Rparser.py',100),
  ('sentence_if -> IF LPAREN condition RPAREN body ELSE LPAREN RPAREN body','sentence_if',9,'p_sentence_if','Rparser.py',101),
  ('conditions -> LOR','conditions',1,'p_conditions','Rparser.py',106),
  ('conditions -> LAND','conditions',1,'p_conditions','Rparser.py',107),
  ('conditions -> LNOT','conditions',1,'p_conditions','Rparser.py',108),
  ('conditions -> LT','conditions',1,'p_conditions','Rparser.py',109),
  ('conditions -> GT','conditions',1,'p_conditions','Rparser.py',110),
  ('conditions -> LE','conditions',1,'p_conditions','Rparser.py',111),
  ('conditions -> GE','conditions',1,'p_conditions','Rparser.py',112),
  ('conditions -> EQ','conditions',1,'p_conditions','Rparser.py',113),
  ('conditions -> NE','conditions',1,'p_conditions','Rparser.py',114),
  ('condition -> expression conditions expression','condition',3,'p_condition','Rparser.py',124),
  ('expression -> condition','expression',1,'p_exprecondition','Rparser.py',129),
  ('declaration -> IDTYPE ID SEMI','declaration',3,'p_declaration','Rparser.py',133),
  ('boolean -> TRUE','boolean',1,'p_booleans','Rparser.py',138),
  ('boolean -> FALSE','boolean',1,'p_booleans','Rparser.py',139),
  ('tvariable -> STRING','tvariable',1,'p_tvariable','Rparser.py',144),
  ('tvariable -> CHARACTER','tvariable',1,'p_tvariable','Rparser.py',145),
  ('tvariable -> boolean','tvariable',1,'p_tvariable','Rparser.py',146),
  ('print -> PRINT tvariable SEMI','print',3,'p_print_statement','Rparser.py',152),
  ('print -> PRINT expression SEMI','print',3,'p_print_statement','Rparser.py',153),
  ('assign -> IDTYPE ID EQUAL tvariable SEMI','assign',5,'p_assign','Rparser.py',162),
  ('assign -> IDTYPE ID EQUAL expression SEMI','assign',5,'p_assign','Rparser.py',163),
  ('assign -> ID EQUAL tvariable SEMI','assign',4,'p_assignre','Rparser.py',169),
  ('assign -> ID EQUAL expression SEMI','assign',4,'p_assignre','Rparser.py',170),
  ('empty -> <empty>','empty',0,'p_empty','Rparser.py',182),
]
