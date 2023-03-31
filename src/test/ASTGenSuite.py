import unittest
from TestUtils import TestAST

class ASTGenSuite(unittest.TestCase):

	def test_500(self):
		input = """k : function void  ( inherit WL : void   , N : array [ 0 , 0 , 8911_9_513_2955 ] of integer     , inherit PH : void   , out jG : void    ) { }    """
		expect = """Program([
	FuncDecl(k, VoidType, [InheritParam(WL, VoidType), Param(N, ArrayType([0, 0, 891195132955], IntegerType)), InheritParam(PH, VoidType), OutParam(jG, VoidType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 500))

	def test_501(self):
		input = """B1UU , Q  : array [ 5 , 24 , 0 ] of boolean    ;   """
		expect = """Program([
	VarDecl(B1UU, ArrayType([5, 24, 0], BooleanType))
	VarDecl(Q, ArrayType([5, 24, 0], BooleanType))
])"""
		self.assertTrue(TestAST.test(input, expect, 501))

	def test_502(self):
		input = """vr : function void  ( inherit out Fc : array [ 9_47067 ] of float     , inherit kuZC : string     ) inherit bP { }    H : function array [ 5 , 85_1 ] of string    ( t : string    , inherit M : array [ 0 , 14293 ] of float     , out w : auto    ) { KjU  = ! k     :: BlC   * MY      ;   continue ;   return f   || W4    >= Wubz   % Dbly      ;   return ;   }    """
		expect = """Program([
	FuncDecl(vr, VoidType, [InheritOutParam(Fc, ArrayType([947067], FloatType)), InheritParam(kuZC, StringType)], bP, BlockStmt([]))
	FuncDecl(H, ArrayType([5, 851], StringType), [Param(t, StringType), InheritParam(M, ArrayType([0, 14293], FloatType)), OutParam(w, AutoType)], None, BlockStmt([AssignStmt(Id(KjU), BinExpr(::, UnExpr(!, Id(k)), BinExpr(*, Id(BlC), Id(MY)))), ContinueStmt(), ReturnStmt(BinExpr(>=, BinExpr(||, Id(f), Id(W4)), BinExpr(%, Id(Wubz), Id(Dbly)))), ReturnStmt()]))
])"""
		self.assertTrue(TestAST.test(input, expect, 502))

	def test_503(self):
		input = """O9 : function string   ( inherit U5i : void   , out fA : auto    ) { }    m  : array [ 43_2_88 , 0 , 0 , 0 ] of float    = ! Q   && rS     - h   % L    / - a      != WV      ;   """
		expect = """Program([
	FuncDecl(O9, StringType, [InheritParam(U5i, VoidType), OutParam(fA, AutoType)], None, BlockStmt([]))
	VarDecl(m, ArrayType([43288, 0, 0, 0], FloatType), BinExpr(!=, BinExpr(&&, UnExpr(!, Id(Q)), BinExpr(-, Id(rS), BinExpr(/, BinExpr(%, Id(h), Id(L)), UnExpr(-, Id(a))))), Id(WV)))
])"""
		self.assertTrue(TestAST.test(input, expect, 503))

# 	def test_504(self):
# 		input = """fH  : auto  = p ( )    - - F     % - IKc    / 8      == W   + Q    || Q   % Q     - TOV     :: ! wjO    || E    / - ia   - kjj         ;   ROyt , b , p , T  : float   ;   """
# 		expect = """Program([
# 	VarDecl(fH, AutoType, BinExpr(::, BinExpr(==, BinExpr(-, FuncCall(p, []), BinExpr(/, BinExpr(%, UnExpr(-, Id(F)), UnExpr(-, Id(IKc))), IntegerLit(8))), BinExpr(||, BinExpr(+, Id(W), Id(Q)), BinExpr(-, BinExpr(%, Id(Q), Id(Q)), Id(TOV)))), BinExpr(||, UnExpr(!, Id(wjO)), BinExpr(-, BinExpr(/, Id(E), UnExpr(-, Id(ia))), Id(kjj)))))
# 	VarDecl(ROyt, FloatType)
# 	VarDecl(b, FloatType)
# 	VarDecl(p, FloatType)
# 	VarDecl(T, FloatType)
# ])"""
# 		self.assertTrue(TestAST.test(input, expect, 504))

	def test_505(self):
		input = """yq : function auto  ( b : array [ 35_54 ] of boolean      ) inherit Y { if ( - us      ) continue ;     }    """
		expect = """Program([
	FuncDecl(yq, AutoType, [Param(b, ArrayType([3554], BooleanType))], Y, BlockStmt([IfStmt(UnExpr(-, Id(us)), ContinueStmt())]))
])"""
		self.assertTrue(TestAST.test(input, expect, 505))

	def test_506(self):
		input = """o : function auto  ( ) inherit M { }    """
		expect = """Program([
	FuncDecl(o, AutoType, [], M, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 506))

	def test_507(self):
		input = """v  : integer   ;   """
		expect = """Program([
	VarDecl(v, IntegerType)
])"""
		self.assertTrue(TestAST.test(input, expect, 507))

	def test_508(self):
		input = """GB : function void  ( ) { EOm , u1  : auto  = x2QAVG3Ef   - cED     :: PV   + S      , ! q    <= - x1     :: ! Hny       ;  l , sz , fe , l , sI , RK2 , Q9  : integer   ;  }    y , ui  : void  ;   i : function array [ 0 ] of float    ( ) inherit K9BYDVS { }    """
		expect = """Program([
	FuncDecl(GB, VoidType, [], None, BlockStmt([VarDecl(EOm, AutoType, BinExpr(::, BinExpr(-, Id(x2QAVG3Ef), Id(cED)), BinExpr(+, Id(PV), Id(S)))), VarDecl(u1, AutoType, BinExpr(::, BinExpr(<=, UnExpr(!, Id(q)), UnExpr(-, Id(x1))), UnExpr(!, Id(Hny)))), VarDecl(l, IntegerType), VarDecl(sz, IntegerType), VarDecl(fe, IntegerType), VarDecl(l, IntegerType), VarDecl(sI, IntegerType), VarDecl(RK2, IntegerType), VarDecl(Q9, IntegerType)]))
	VarDecl(y, VoidType)
	VarDecl(ui, VoidType)
	FuncDecl(i, ArrayType([0], FloatType), [], K9BYDVS, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 508))

	def test_509(self):
		input = """R9OMi  : boolean   = - dZ0   || gxxQ     - - x5    || hj   / Q      < ! VJD    / Lm   - O     / 7235933        ;   """
		expect = """Program([
	VarDecl(R9OMi, BooleanType, BinExpr(<, BinExpr(||, BinExpr(||, UnExpr(-, Id(dZ0)), BinExpr(-, Id(gxxQ), UnExpr(-, Id(x5)))), BinExpr(/, Id(hj), Id(Q))), BinExpr(-, BinExpr(/, UnExpr(!, Id(VJD)), Id(Lm)), BinExpr(/, Id(O), IntegerLit(7235933)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 509))

	def test_510(self):
		input = """jGcFI : function void  ( ) { }    f : function array [ 0 , 0 , 44_004_933 , 0 , 0 , 0 , 0 , 0 , 0 ] of boolean    ( ) inherit rQJ { }    """
		expect = """Program([
	FuncDecl(jGcFI, VoidType, [], None, BlockStmt([]))
	FuncDecl(f, ArrayType([0, 0, 44004933, 0, 0, 0, 0, 0, 0], BooleanType), [], rQJ, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 510))

	def test_511(self):
		input = """I_ : function float   ( ) inherit dbB { y , L , Ca , W  : integer   ;  }    """
		expect = """Program([
	FuncDecl(I_, FloatType, [], dbB, BlockStmt([VarDecl(y, IntegerType), VarDecl(L, IntegerType), VarDecl(Ca, IntegerType), VarDecl(W, IntegerType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 511))

	def test_512(self):
		input = """H : function array [ 3 , 2_06 , 0 ] of float    ( ) { }    """
		expect = """Program([
	FuncDecl(H, ArrayType([3, 206, 0], FloatType), [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 512))

	def test_513(self):
		input = """m  : auto  = Hl   + in9    / O   * g     - ! Ld   || A      > ! 7     && { }       :: KxKT   - OdH    + Fv   * Fb     || zY   % gD    + b ( )      != - d   || j     - Eo   || T    && e   + YW         ;   """
		expect = """Program([
	VarDecl(m, AutoType, BinExpr(::, BinExpr(>, BinExpr(||, BinExpr(-, BinExpr(+, Id(Hl), BinExpr(*, BinExpr(/, Id(in9), Id(O)), Id(g))), UnExpr(!, Id(Ld))), Id(A)), BinExpr(&&, UnExpr(!, IntegerLit(7)), ArrayLit([]))), BinExpr(!=, BinExpr(||, BinExpr(+, BinExpr(-, Id(KxKT), Id(OdH)), BinExpr(*, Id(Fv), Id(Fb))), BinExpr(+, BinExpr(%, Id(zY), Id(gD)), FuncCall(b, []))), BinExpr(&&, BinExpr(||, BinExpr(||, UnExpr(-, Id(d)), BinExpr(-, Id(j), Id(Eo))), Id(T)), BinExpr(+, Id(e), Id(YW))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 513))

	def test_514(self):
		input = """wGmO8 : function boolean   ( inherit ow : integer     ) { }    A : function array [ 0 , 0 ] of boolean    ( ) inherit lDiO { for ( aW7  = ! z78     :: - m    != ! m      , f   <= ""     :: Z   - e      , ! i    <= o4g9   - A     :: ! hX      ) return ;     }    _ : function auto  ( ) inherit x9j2I { }    """
		expect = """Program([
	FuncDecl(wGmO8, BooleanType, [InheritParam(ow, IntegerType)], None, BlockStmt([]))
	FuncDecl(A, ArrayType([0, 0], BooleanType), [], lDiO, BlockStmt([ForStmt(AssignStmt(Id(aW7), BinExpr(::, UnExpr(!, Id(z78)), BinExpr(!=, UnExpr(-, Id(m)), UnExpr(!, Id(m))))), BinExpr(::, BinExpr(<=, Id(f), StringLit()), BinExpr(-, Id(Z), Id(e))), BinExpr(::, BinExpr(<=, UnExpr(!, Id(i)), BinExpr(-, Id(o4g9), Id(A))), UnExpr(!, Id(hX))), ReturnStmt())]))
	FuncDecl(_, AutoType, [], x9j2I, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 514))

	def test_515(self):
		input = """Lq : function auto  ( out Lj : integer    , vy1B : auto   , out u : void    ) inherit sFEd { if ( ! P     :: ""      ) break ;     }    hI6t : function array [ 7 , 0 , 0 , 58_573_043_52_56_9_0 , 70 , 1036 ] of float    ( inherit FA : auto   , inherit l : auto   , inherit he : void    ) inherit E5 { return o08Uh   % X      ;   { }   }    """
		expect = """Program([
	FuncDecl(Lq, AutoType, [OutParam(Lj, IntegerType), Param(vy1B, AutoType), OutParam(u, VoidType)], sFEd, BlockStmt([IfStmt(BinExpr(::, UnExpr(!, Id(P)), StringLit()), BreakStmt())]))
	FuncDecl(hI6t, ArrayType([7, 0, 0, 58573043525690, 70, 1036], FloatType), [InheritParam(FA, AutoType), InheritParam(l, AutoType), InheritParam(he, VoidType)], E5, BlockStmt([ReturnStmt(BinExpr(%, Id(o08Uh), Id(X))), BlockStmt([])]))
])"""
		self.assertTrue(TestAST.test(input, expect, 515))

	def test_516(self):
		input = """hsLU : function array [ 0 ] of string    ( ) inherit n { }    """
		expect = """Program([
	FuncDecl(hsLU, ArrayType([0], StringType), [], n, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 516))

	def test_517(self):
		input = """iti , V  : auto  ;   """
		expect = """Program([
	VarDecl(iti, AutoType)
	VarDecl(V, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 517))

	def test_518(self):
		input = """p  : string   = X ( )    - ! A   || bF      == ! ! - qdX         ;   """
		expect = """Program([
	VarDecl(p, StringType, BinExpr(==, BinExpr(||, BinExpr(-, FuncCall(X, []), UnExpr(!, Id(A))), Id(bF)), UnExpr(!, UnExpr(!, UnExpr(-, Id(qdX))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 518))

	def test_519(self):
		input = """fbL_M1_F  : string   ;   E : function void  ( out J8 : void    ) { WD  : array [ 402532191 , 0 , 7_6 ] of float    = Z16L5   * b       ;  { }   }    B  : integer   ;   Yx  : string   = ! - f    + _B   || ub       :: B1g   || cMQ    - - P     / - W    + - eKqg         ;   """
		expect = """Program([
	VarDecl(fbL_M1_F, StringType)
	FuncDecl(E, VoidType, [OutParam(J8, VoidType)], None, BlockStmt([VarDecl(WD, ArrayType([402532191, 0, 76], FloatType), BinExpr(*, Id(Z16L5), Id(b))), BlockStmt([])]))
	VarDecl(B, IntegerType)
	VarDecl(Yx, StringType, BinExpr(::, BinExpr(||, BinExpr(+, UnExpr(!, UnExpr(-, Id(f))), Id(_B)), Id(ub)), BinExpr(||, Id(B1g), BinExpr(+, BinExpr(-, Id(cMQ), BinExpr(/, UnExpr(-, Id(P)), UnExpr(-, Id(W)))), UnExpr(-, Id(eKqg))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 519))

	def test_520(self):
		input = """S : function auto  ( ) inherit IiE { }    """
		expect = """Program([
	FuncDecl(S, AutoType, [], IiE, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 520))

	def test_521(self):
		input = """n1 : function void  ( inherit out pj : string     ) { B5p  : void  = FY   || pv    == x   * H1     :: ai ( )       ;  }    """
		expect = """Program([
	FuncDecl(n1, VoidType, [InheritOutParam(pj, StringType)], None, BlockStmt([VarDecl(B5p, VoidType, BinExpr(::, BinExpr(==, BinExpr(||, Id(FY), Id(pv)), BinExpr(*, Id(x), Id(H1))), FuncCall(ai, [])))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 521))

	def test_522(self):
		input = """h  : void  = { }     % - fICF   % GtY9      < f_ ( )    || VPU   && SOG    % U   / un       :: - e   * R    || ! H1      == ! ! ""         ;   """
		expect = """Program([
	VarDecl(h, VoidType, BinExpr(::, BinExpr(<, BinExpr(%, BinExpr(%, ArrayLit([]), UnExpr(-, Id(fICF))), Id(GtY9)), BinExpr(&&, BinExpr(||, FuncCall(f_, []), Id(VPU)), BinExpr(/, BinExpr(%, Id(SOG), Id(U)), Id(un)))), BinExpr(==, BinExpr(||, BinExpr(*, UnExpr(-, Id(e)), Id(R)), UnExpr(!, Id(H1))), UnExpr(!, UnExpr(!, StringLit())))))
])"""
		self.assertTrue(TestAST.test(input, expect, 522))

	def test_523(self):
		input = """jYns : function void  ( ) inherit r { }    CY  : void  = - D8    - y    > ! ""     % ! e7    * e   + l         ;   B  : string   = - - i ( )         ;   yX , Mft , v , lGf , r , eR  : string   ;   """
		expect = """Program([
	FuncDecl(jYns, VoidType, [], r, BlockStmt([]))
	VarDecl(CY, VoidType, BinExpr(>, BinExpr(-, UnExpr(-, Id(D8)), Id(y)), BinExpr(+, BinExpr(*, BinExpr(%, UnExpr(!, StringLit()), UnExpr(!, Id(e7))), Id(e)), Id(l))))
	VarDecl(B, StringType, UnExpr(-, UnExpr(-, FuncCall(i, []))))
	VarDecl(yX, StringType)
	VarDecl(Mft, StringType)
	VarDecl(v, StringType)
	VarDecl(lGf, StringType)
	VarDecl(r, StringType)
	VarDecl(eR, StringType)
])"""
		self.assertTrue(TestAST.test(input, expect, 523))

	def test_524(self):
		input = """GC1X2v , y , id  : string   ;   H , ki , yud7mJ  : auto  ;   V : function auto  ( inherit out F : array [ 4_6_27 ] of boolean     , inherit out VV : string    , out a : string    , inherit lZpN : array [ 0 , 99_9_537_3_272_4_6_2_5_5 ] of boolean      ) { }    """
		expect = """Program([
	VarDecl(GC1X2v, StringType)
	VarDecl(y, StringType)
	VarDecl(id, StringType)
	VarDecl(H, AutoType)
	VarDecl(ki, AutoType)
	VarDecl(yud7mJ, AutoType)
	FuncDecl(V, AutoType, [InheritOutParam(F, ArrayType([4627], BooleanType)), InheritOutParam(VV, StringType), OutParam(a, StringType), InheritParam(lZpN, ArrayType([0, 999537327246255], BooleanType))], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 524))

	def test_525(self):
		input = """FsY : function integer   ( inherit out yD : array [ 73 , 0 ] of integer      ) { NJA  : auto  ;  }    Tg : function array [ 700_91_839 ] of string    ( ) inherit Ay { do { }  while ( ! Eii    != TU     ) ;   t  = - h    < j   + a0M     :: pF ( )    >= - K3      ;   }    T  : array [ 0 , 1_4_83 , 0 ] of boolean    ;   Y  : array [ 58 ] of boolean    ;   """
		expect = """Program([
	FuncDecl(FsY, IntegerType, [InheritOutParam(yD, ArrayType([73, 0], IntegerType))], None, BlockStmt([VarDecl(NJA, AutoType)]))
	FuncDecl(Tg, ArrayType([70091839], StringType), [], Ay, BlockStmt([DoWhileStmt(BinExpr(!=, UnExpr(!, Id(Eii)), Id(TU)), BlockStmt([])), AssignStmt(Id(t), BinExpr(::, BinExpr(<, UnExpr(-, Id(h)), BinExpr(+, Id(j), Id(a0M))), BinExpr(>=, FuncCall(pF, []), UnExpr(-, Id(K3)))))]))
	VarDecl(T, ArrayType([0, 1483, 0], BooleanType))
	VarDecl(Y, ArrayType([58], BooleanType))
])"""
		self.assertTrue(TestAST.test(input, expect, 525))

	def test_526(self):
		input = """m , W , h  : array [ 0 ] of integer    = - k   && U     % heA   + ""        , 7    || ! r     + 4    || h ( )        , ! T   && F     + QwCMbpT    >= - - Hjm    && t   - q       :: D      ;   """
		expect = """Program([
	VarDecl(m, ArrayType([0], IntegerType), BinExpr(&&, UnExpr(-, Id(k)), BinExpr(+, BinExpr(%, Id(U), Id(heA)), StringLit())))
	VarDecl(W, ArrayType([0], IntegerType), BinExpr(||, BinExpr(||, IntegerLit(7), BinExpr(+, UnExpr(!, Id(r)), IntegerLit(4))), FuncCall(h, [])))
	VarDecl(h, ArrayType([0], IntegerType), BinExpr(::, BinExpr(>=, BinExpr(&&, UnExpr(!, Id(T)), BinExpr(+, Id(F), Id(QwCMbpT))), BinExpr(&&, UnExpr(-, UnExpr(-, Id(Hjm))), BinExpr(-, Id(t), Id(q)))), Id(D)))
])"""
		self.assertTrue(TestAST.test(input, expect, 526))

	def test_527(self):
		input = """d : function boolean   ( cV : array [ 0 ] of integer      ) { }    """
		expect = """Program([
	FuncDecl(d, BooleanType, [Param(cV, ArrayType([0], IntegerType))], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 527))

	def test_528(self):
		input = """C , kgd362 , TWW , B  : array [ 0 ] of boolean    ;   """
		expect = """Program([
	VarDecl(C, ArrayType([0], BooleanType))
	VarDecl(kgd362, ArrayType([0], BooleanType))
	VarDecl(TWW, ArrayType([0], BooleanType))
	VarDecl(B, ArrayType([0], BooleanType))
])"""
		self.assertTrue(TestAST.test(input, expect, 528))

	def test_529(self):
		input = """Z4ml4f : function void  ( ) { }    """
		expect = """Program([
	FuncDecl(Z4ml4f, VoidType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 529))

	def test_530(self):
		input = """Sw : function void  ( ) inherit N { }    """
		expect = """Program([
	FuncDecl(Sw, VoidType, [], N, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 530))

	def test_531(self):
		input = """Fh : function void  ( ) { while ( - rU    >= n   / sVhb      ) break ;     }    tvlz2  : auto  ;   v  : void  ;   d  : auto  ;   b : function void  ( ) inherit X3ZH5 { return P   * BV      ;   }    """
		expect = """Program([
	FuncDecl(Fh, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(>=, UnExpr(-, Id(rU)), BinExpr(/, Id(n), Id(sVhb))), BreakStmt())]))
	VarDecl(tvlz2, AutoType)
	VarDecl(v, VoidType)
	VarDecl(d, AutoType)
	FuncDecl(b, VoidType, [], X3ZH5, BlockStmt([ReturnStmt(BinExpr(*, Id(P), Id(BV)))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 531))

	def test_532(self):
		input = """Z5_I9 : function void  ( inherit Q : array [ 61_8_4 ] of boolean     , rBK4 : array [ 0 , 8 , 2 ] of string      ) { q  : auto  ;  gGe , X  : void  ;  }    """
		expect = """Program([
	FuncDecl(Z5_I9, VoidType, [InheritParam(Q, ArrayType([6184], BooleanType)), Param(rBK4, ArrayType([0, 8, 2], StringType))], None, BlockStmt([VarDecl(q, AutoType), VarDecl(gGe, VoidType), VarDecl(X, VoidType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 532))

	def test_533(self):
		input = """h : function void  ( M : array [ 177_65_80_8510894 ] of string     , inherit R : float     ) { JItg  : auto  ;  F  : void  = XNc   * TV    <= ! It       ;  }    _ , o  : boolean   ;   y  : void  = ! ! Wr3     && ! k   || wO96         ;   g , mc , B  : void  ;   """
		expect = """Program([
	FuncDecl(h, VoidType, [Param(M, ArrayType([17765808510894], StringType)), InheritParam(R, FloatType)], None, BlockStmt([VarDecl(JItg, AutoType), VarDecl(F, VoidType, BinExpr(<=, BinExpr(*, Id(XNc), Id(TV)), UnExpr(!, Id(It))))]))
	VarDecl(_, BooleanType)
	VarDecl(o, BooleanType)
	VarDecl(y, VoidType, BinExpr(||, BinExpr(&&, UnExpr(!, UnExpr(!, Id(Wr3))), UnExpr(!, Id(k))), Id(wO96)))
	VarDecl(g, VoidType)
	VarDecl(mc, VoidType)
	VarDecl(B, VoidType)
])"""
		self.assertTrue(TestAST.test(input, expect, 533))

	def test_534(self):
		input = """l , tY  : void  = - mZiy    && 6     % - V    || BO   * E      <= wH   * L    + s   / v     + ! k    % krh   * upf        , abs   || v    - AsD   || nL2     + e   && OXzx    && - l      >= ! 8    + s   || zP       :: - Y   || d    + - N      == u      ;   txT , s , lmZ , fbO7  : auto  ;   """
		expect = """Program([
	VarDecl(l, VoidType, BinExpr(<=, BinExpr(||, BinExpr(&&, UnExpr(-, Id(mZiy)), BinExpr(%, IntegerLit(6), UnExpr(-, Id(V)))), BinExpr(*, Id(BO), Id(E))), BinExpr(+, BinExpr(+, BinExpr(*, Id(wH), Id(L)), BinExpr(/, Id(s), Id(v))), BinExpr(*, BinExpr(%, UnExpr(!, Id(k)), Id(krh)), Id(upf)))))
	VarDecl(tY, VoidType, BinExpr(::, BinExpr(>=, BinExpr(&&, BinExpr(&&, BinExpr(||, BinExpr(||, Id(abs), BinExpr(-, Id(v), Id(AsD))), BinExpr(+, Id(nL2), Id(e))), Id(OXzx)), UnExpr(-, Id(l))), BinExpr(||, BinExpr(+, UnExpr(!, IntegerLit(8)), Id(s)), Id(zP))), BinExpr(==, BinExpr(||, UnExpr(-, Id(Y)), BinExpr(+, Id(d), UnExpr(-, Id(N)))), Id(u))))
	VarDecl(txT, AutoType)
	VarDecl(s, AutoType)
	VarDecl(lmZ, AutoType)
	VarDecl(fbO7, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 534))

	def test_535(self):
		input = """BL6 : function string   ( ) { d ( )  ;   FP  : array [ 0 , 0 ] of integer    = ! f       ;  }    EStJm , D , w  : float   ;   """
		expect = """Program([
	FuncDecl(BL6, StringType, [], None, BlockStmt([CallStmt(d, ), VarDecl(FP, ArrayType([0, 0], IntegerType), UnExpr(!, Id(f)))]))
	VarDecl(EStJm, FloatType)
	VarDecl(D, FloatType)
	VarDecl(w, FloatType)
])"""
		self.assertTrue(TestAST.test(input, expect, 535))

	def test_536(self):
		input = """R : function void  ( ) inherit DZ { }    """
		expect = """Program([
	FuncDecl(R, VoidType, [], DZ, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 536))

	def test_537(self):
		input = """YFaYT , d , yi  : auto  ;   """
		expect = """Program([
	VarDecl(YFaYT, AutoType)
	VarDecl(d, AutoType)
	VarDecl(yi, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 537))

	def test_538(self):
		input = """A , D , A  : array [ 0 , 0 , 9 ] of string    ;   ck , wB , dp  : array [ 6 ] of boolean    ;   """
		expect = """Program([
	VarDecl(A, ArrayType([0, 0, 9], StringType))
	VarDecl(D, ArrayType([0, 0, 9], StringType))
	VarDecl(A, ArrayType([0, 0, 9], StringType))
	VarDecl(ck, ArrayType([6], BooleanType))
	VarDecl(wB, ArrayType([6], BooleanType))
	VarDecl(dp, ArrayType([6], BooleanType))
])"""
		self.assertTrue(TestAST.test(input, expect, 538))

	def test_539(self):
		input = """Fl , n  : array [ 0 ] of string    ;   DmwsYhA : function array [ 89 ] of float    ( ) inherit Kx { continue ;   by6 , U , a  : array [ 0 , 2 , 9930 , 8_0 , 778_9886_1 , 0 , 34_86901 ] of integer    ;  dF9  = R   + Fp      ;   m82  : boolean   = W   || weC    > ! xv       ;  }    yT2 : function auto  ( ) inherit Cx { }    b : function auto  ( inherit i3 : boolean     ) inherit QY { kW  : void  = ""    < M   * GXAkG       ;  }    """
		expect = """Program([
	VarDecl(Fl, ArrayType([0], StringType))
	VarDecl(n, ArrayType([0], StringType))
	FuncDecl(DmwsYhA, ArrayType([89], FloatType), [], Kx, BlockStmt([ContinueStmt(), VarDecl(by6, ArrayType([0, 2, 9930, 80, 77898861, 0, 3486901], IntegerType)), VarDecl(U, ArrayType([0, 2, 9930, 80, 77898861, 0, 3486901], IntegerType)), VarDecl(a, ArrayType([0, 2, 9930, 80, 77898861, 0, 3486901], IntegerType)), AssignStmt(Id(dF9), BinExpr(+, Id(R), Id(Fp))), VarDecl(m82, BooleanType, BinExpr(>, BinExpr(||, Id(W), Id(weC)), UnExpr(!, Id(xv))))]))
	FuncDecl(yT2, AutoType, [], Cx, BlockStmt([]))
	FuncDecl(b, AutoType, [InheritParam(i3, BooleanType)], QY, BlockStmt([VarDecl(kW, VoidType, BinExpr(<, StringLit(), BinExpr(*, Id(M), Id(GXAkG))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 539))

	def test_540(self):
		input = """YGr : function auto  ( ) inherit Jxgm { C , LNO , _  : float   = ""     :: - Q      , - Qi      , I   % Y       ;  }    a : function void  ( out tN : integer     ) { zvj3 , vH8  : array [ 0 ] of integer    = h     , - PY    >= nA   - u       ;  }    W  : string   ;   RyB : function integer   ( inherit out p3y : void    ) { break ;   { break ;   }   { }   if ( kPV   - W    <= d   % HU     :: fr   || zN      ) continue ;     }    g , Xas  : array [ 0 , 0 , 0 , 0 , 0 ] of integer    ;   """
		expect = """Program([
	FuncDecl(YGr, AutoType, [], Jxgm, BlockStmt([VarDecl(C, FloatType, BinExpr(::, StringLit(), UnExpr(-, Id(Q)))), VarDecl(LNO, FloatType, UnExpr(-, Id(Qi))), VarDecl(_, FloatType, BinExpr(%, Id(I), Id(Y)))]))
	FuncDecl(a, VoidType, [OutParam(tN, IntegerType)], None, BlockStmt([VarDecl(zvj3, ArrayType([0], IntegerType), Id(h)), VarDecl(vH8, ArrayType([0], IntegerType), BinExpr(>=, UnExpr(-, Id(PY)), BinExpr(-, Id(nA), Id(u))))]))
	VarDecl(W, StringType)
	FuncDecl(RyB, IntegerType, [InheritOutParam(p3y, VoidType)], None, BlockStmt([BreakStmt(), BlockStmt([BreakStmt()]), BlockStmt([]), IfStmt(BinExpr(::, BinExpr(<=, BinExpr(-, Id(kPV), Id(W)), BinExpr(%, Id(d), Id(HU))), BinExpr(||, Id(fr), Id(zN))), ContinueStmt())]))
	VarDecl(g, ArrayType([0, 0, 0, 0, 0], IntegerType))
	VarDecl(Xas, ArrayType([0, 0, 0, 0, 0], IntegerType))
])"""
		self.assertTrue(TestAST.test(input, expect, 540))

	def test_541(self):
		input = """SE : function float   ( inherit n5 : auto   , inherit out x : auto    ) inherit MW { }    j  : string   = ! ! hIz     && c5    > true       ;   z : function array [ 0 ] of float    ( ) { }    GzhVt  : array [ 1 ] of string    = UV ( )    >= ! e   || Wsq    / - L         ;   P : function void  ( hd : array [ 0 ] of boolean     , out vU : void   , inherit out d : void    ) { }    """
		expect = """Program([
	FuncDecl(SE, FloatType, [InheritParam(n5, AutoType), InheritOutParam(x, AutoType)], MW, BlockStmt([]))
	VarDecl(j, StringType, BinExpr(>, BinExpr(&&, UnExpr(!, UnExpr(!, Id(hIz))), Id(c5)), BooleanLit(True)))
	FuncDecl(z, ArrayType([0], FloatType), [], None, BlockStmt([]))
	VarDecl(GzhVt, ArrayType([1], StringType), BinExpr(>=, FuncCall(UV, []), BinExpr(||, UnExpr(!, Id(e)), BinExpr(/, Id(Wsq), UnExpr(-, Id(L))))))
	FuncDecl(P, VoidType, [Param(hd, ArrayType([0], BooleanType)), OutParam(vU, VoidType), InheritOutParam(d, VoidType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 541))

	def test_542(self):
		input = """w : function auto  ( ) inherit Og { }    w : function array [ 71 , 4 , 0 ] of string    ( inherit out rM : auto   , inherit out T : void   , inherit y : void    ) { for ( l  = - e      , Qj   + D4    >= kno ( )      , fUmx4   || p    != sYw   && up     :: IA   != jR   * l      ) continue ;     v27 , h49  : integer   = - f    < S   * G     :: - Jm      , xWv   + dixOfXl6       ;  }    Dh : function float   ( inherit out QaL : void    ) inherit A { }    t , UEX , h6Nup , W7  : array [ 2 , 0 , 5_032_8 ] of string    ;   R : function void  ( ) { do { }  while ( D ( )      ) ;   }    Cl7b : function void  ( p : array [ 0 , 0 , 0 , 0 , 2 , 8 ] of boolean      ) inherit gT { }    U , x  : void  = y ( )     :: - ""    % gDo7S ( )        , - - q9    + 8       :: K ( )       ;   s1 : function void  ( ) { }    """
		expect = """Program([
	FuncDecl(w, AutoType, [], Og, BlockStmt([]))
	FuncDecl(w, ArrayType([71, 4, 0], StringType), [InheritOutParam(rM, AutoType), InheritOutParam(T, VoidType), InheritParam(y, VoidType)], None, BlockStmt([ForStmt(AssignStmt(Id(l), UnExpr(-, Id(e))), BinExpr(>=, BinExpr(+, Id(Qj), Id(D4)), FuncCall(kno, [])), BinExpr(::, BinExpr(!=, BinExpr(||, Id(fUmx4), Id(p)), BinExpr(&&, Id(sYw), Id(up))), BinExpr(!=, Id(IA), BinExpr(*, Id(jR), Id(l)))), ContinueStmt()), VarDecl(v27, IntegerType, BinExpr(::, BinExpr(<, UnExpr(-, Id(f)), BinExpr(*, Id(S), Id(G))), UnExpr(-, Id(Jm)))), VarDecl(h49, IntegerType, BinExpr(+, Id(xWv), Id(dixOfXl6)))]))
	FuncDecl(Dh, FloatType, [InheritOutParam(QaL, VoidType)], A, BlockStmt([]))
	VarDecl(t, ArrayType([2, 0, 50328], StringType))
	VarDecl(UEX, ArrayType([2, 0, 50328], StringType))
	VarDecl(h6Nup, ArrayType([2, 0, 50328], StringType))
	VarDecl(W7, ArrayType([2, 0, 50328], StringType))
	FuncDecl(R, VoidType, [], None, BlockStmt([DoWhileStmt(FuncCall(D, []), BlockStmt([]))]))
	FuncDecl(Cl7b, VoidType, [Param(p, ArrayType([0, 0, 0, 0, 2, 8], BooleanType))], gT, BlockStmt([]))
	VarDecl(U, VoidType, BinExpr(::, FuncCall(y, []), BinExpr(%, UnExpr(-, StringLit()), FuncCall(gDo7S, []))))
	VarDecl(x, VoidType, BinExpr(::, BinExpr(+, UnExpr(-, UnExpr(-, Id(q9))), IntegerLit(8)), FuncCall(K, [])))
	FuncDecl(s1, VoidType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 542))

	def test_543(self):
		input = """MP : function void  ( ) { g  = n   - FKw     :: bo   && hU      ;   }    """
		expect = """Program([
	FuncDecl(MP, VoidType, [], None, BlockStmt([AssignStmt(Id(g), BinExpr(::, BinExpr(-, Id(n), Id(FKw)), BinExpr(&&, Id(bo), Id(hU))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 543))

	def test_544(self):
		input = """Z7 : function void  ( inherit out Bu : void    ) { }    """
		expect = """Program([
	FuncDecl(Z7, VoidType, [InheritOutParam(Bu, VoidType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 544))

	def test_545(self):
		input = """l : function integer   ( ) inherit wm { }    """
		expect = """Program([
	FuncDecl(l, IntegerType, [], wm, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 545))

	def test_546(self):
		input = """J : function void  ( inherit out G : auto    ) inherit B { }    """
		expect = """Program([
	FuncDecl(J, VoidType, [InheritOutParam(G, AutoType)], B, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 546))

	def test_547(self):
		input = """vW , we  : auto  = Sd   / zFD    - W   / _s9     - ! D    && gf   && D60G       :: j   || p    % NW    && ! d    && g   && G      == ! - vsr     / z2   * LxA    / yOOw   + N        , f   + u    + gH    || ""    + H   && A0      == - c   && U    * - jbyftp       :: N   + WYJ    + cWX   && S     - 4        ;   X : function integer   ( B : void    ) inherit Nb { X  : auto  ;  }    YE  : void  ;   """
		expect = """Program([
	VarDecl(vW, AutoType, BinExpr(::, BinExpr(&&, BinExpr(&&, BinExpr(-, BinExpr(-, BinExpr(/, Id(Sd), Id(zFD)), BinExpr(/, Id(W), Id(_s9))), UnExpr(!, Id(D))), Id(gf)), Id(D60G)), BinExpr(==, BinExpr(&&, BinExpr(&&, BinExpr(&&, BinExpr(||, Id(j), BinExpr(%, Id(p), Id(NW))), UnExpr(!, Id(d))), Id(g)), Id(G)), BinExpr(+, BinExpr(/, BinExpr(*, BinExpr(/, UnExpr(!, UnExpr(-, Id(vsr))), Id(z2)), Id(LxA)), Id(yOOw)), Id(N)))))
	VarDecl(we, AutoType, BinExpr(::, BinExpr(==, BinExpr(&&, BinExpr(||, BinExpr(+, BinExpr(+, Id(f), Id(u)), Id(gH)), BinExpr(+, StringLit(), Id(H))), Id(A0)), BinExpr(&&, UnExpr(-, Id(c)), BinExpr(*, Id(U), UnExpr(-, Id(jbyftp))))), BinExpr(&&, BinExpr(+, BinExpr(+, Id(N), Id(WYJ)), Id(cWX)), BinExpr(-, Id(S), IntegerLit(4)))))
	FuncDecl(X, IntegerType, [Param(B, VoidType)], Nb, BlockStmt([VarDecl(X, AutoType)]))
	VarDecl(YE, VoidType)
])"""
		self.assertTrue(TestAST.test(input, expect, 547))

	def test_548(self):
		input = """E7UQEX , Q , E , y  : array [ 8 ] of integer    = R8Xe0j   * b    || u   / eoP     || ! n   % mAM       :: qMuF ( )      , ! ! ! LUI      > ! 5     && o ( )       , - A   && G     % ! G    / PBFqn   + hp      < ! ! p     || { }       :: r   - m ( )    / ! j7KX      == - JO_Y    || _8 ( )     % - qe   && lI2        , B7N   - V    + - Jrp     && ! H    / ! Y      > - - XCM   || N         ;   hy : function array [ 0 , 2 , 4487_96 ] of boolean    ( x : void    ) inherit C { Z  : array [ 0 , 0 ] of float    = ""    != p   + O5       ;  gU , I , jLQcPT , C , L , k , U3  : void  ;  return Mc   + UhEA6     :: X_   == m   + ojMz      ;   }    BU  : void  ;   """
		expect = """Program([
	VarDecl(E7UQEX, ArrayType([8], IntegerType), BinExpr(::, BinExpr(||, BinExpr(||, BinExpr(*, Id(R8Xe0j), Id(b)), BinExpr(/, Id(u), Id(eoP))), BinExpr(%, UnExpr(!, Id(n)), Id(mAM))), FuncCall(qMuF, [])))
	VarDecl(Q, ArrayType([8], IntegerType), BinExpr(>, UnExpr(!, UnExpr(!, UnExpr(!, Id(LUI)))), BinExpr(&&, UnExpr(!, IntegerLit(5)), FuncCall(o, []))))
	VarDecl(E, ArrayType([8], IntegerType), BinExpr(::, BinExpr(<, BinExpr(&&, UnExpr(-, Id(A)), BinExpr(+, BinExpr(/, BinExpr(%, Id(G), UnExpr(!, Id(G))), Id(PBFqn)), Id(hp))), BinExpr(||, UnExpr(!, UnExpr(!, Id(p))), ArrayLit([]))), BinExpr(==, BinExpr(-, Id(r), BinExpr(/, FuncCall(m, []), UnExpr(!, Id(j7KX)))), BinExpr(&&, BinExpr(||, UnExpr(-, Id(JO_Y)), BinExpr(%, FuncCall(_8, []), UnExpr(-, Id(qe)))), Id(lI2)))))
	VarDecl(y, ArrayType([8], IntegerType), BinExpr(>, BinExpr(&&, BinExpr(+, BinExpr(-, Id(B7N), Id(V)), UnExpr(-, Id(Jrp))), BinExpr(/, UnExpr(!, Id(H)), UnExpr(!, Id(Y)))), BinExpr(||, UnExpr(-, UnExpr(-, Id(XCM))), Id(N))))
	FuncDecl(hy, ArrayType([0, 2, 448796], BooleanType), [Param(x, VoidType)], C, BlockStmt([VarDecl(Z, ArrayType([0, 0], FloatType), BinExpr(!=, StringLit(), BinExpr(+, Id(p), Id(O5)))), VarDecl(gU, VoidType), VarDecl(I, VoidType), VarDecl(jLQcPT, VoidType), VarDecl(C, VoidType), VarDecl(L, VoidType), VarDecl(k, VoidType), VarDecl(U3, VoidType), ReturnStmt(BinExpr(::, BinExpr(+, Id(Mc), Id(UhEA6)), BinExpr(==, Id(X_), BinExpr(+, Id(m), Id(ojMz)))))]))
	VarDecl(BU, VoidType)
])"""
		self.assertTrue(TestAST.test(input, expect, 548))

	def test_549(self):
		input = """j  : array [ 0 ] of integer    ;   G : function integer   ( ) inherit s { do { }  while ( - H_     :: R   && md      ) ;   break ;   }    """
		expect = """Program([
	VarDecl(j, ArrayType([0], IntegerType))
	FuncDecl(G, IntegerType, [], s, BlockStmt([DoWhileStmt(BinExpr(::, UnExpr(-, Id(H_)), BinExpr(&&, Id(R), Id(md))), BlockStmt([])), BreakStmt()]))
])"""
		self.assertTrue(TestAST.test(input, expect, 549))

	def test_550(self):
		input = """dZ : function array [ 80 ] of boolean    ( ) inherit TFfj { }    """
		expect = """Program([
	FuncDecl(dZ, ArrayType([80], BooleanType), [], TFfj, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 550))

	def test_551(self):
		input = """HQ : function void  ( H : void    ) { }    o9B : function integer   ( F : void    ) inherit a { F  : integer   ;  }    """
		expect = """Program([
	FuncDecl(HQ, VoidType, [Param(H, VoidType)], None, BlockStmt([]))
	FuncDecl(o9B, IntegerType, [Param(F, VoidType)], a, BlockStmt([VarDecl(F, IntegerType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 551))

	def test_552(self):
		input = """VWv : function array [ 2_3 ] of integer    ( inherit out D : array [ 0 ] of string      ) { f , x  : void  = jNh   && VRWh     :: j   || D      , W   - aw    > ! f     :: ""    >= wye   * Zm       ;  break ;   }    w : function auto  ( out qT : auto    ) inherit x2 { }    A : function auto  ( inherit out iALD : auto    ) { }    """
		expect = """Program([
	FuncDecl(VWv, ArrayType([23], IntegerType), [InheritOutParam(D, ArrayType([0], StringType))], None, BlockStmt([VarDecl(f, VoidType, BinExpr(::, BinExpr(&&, Id(jNh), Id(VRWh)), BinExpr(||, Id(j), Id(D)))), VarDecl(x, VoidType, BinExpr(::, BinExpr(>, BinExpr(-, Id(W), Id(aw)), UnExpr(!, Id(f))), BinExpr(>=, StringLit(), BinExpr(*, Id(wye), Id(Zm))))), BreakStmt()]))
	FuncDecl(w, AutoType, [OutParam(qT, AutoType)], x2, BlockStmt([]))
	FuncDecl(A, AutoType, [InheritOutParam(iALD, AutoType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 552))

	def test_553(self):
		input = """A : function void  ( out FI5d : string     ) { }    """
		expect = """Program([
	FuncDecl(A, VoidType, [OutParam(FI5d, StringType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 553))

	def test_554(self):
		input = """c : function integer   ( ) { }    U : function auto  ( inherit o : auto    ) inherit HX { if ( ! J    >= - J      ) { z ( )  ;   ro , Im  : float   ;  Ge  : auto  ;  OmFJ  : auto  ;  }     UTB , SN  : array [ 621_45_330_2_0 , 0 , 0 , 205 ] of string    = Y   || d     :: Br6   > - w      , kBDlJ0W   * H    > ! Ep       ;  }    """
		expect = """Program([
	FuncDecl(c, IntegerType, [], None, BlockStmt([]))
	FuncDecl(U, AutoType, [InheritParam(o, AutoType)], HX, BlockStmt([IfStmt(BinExpr(>=, UnExpr(!, Id(J)), UnExpr(-, Id(J))), BlockStmt([CallStmt(z, ), VarDecl(ro, FloatType), VarDecl(Im, FloatType), VarDecl(Ge, AutoType), VarDecl(OmFJ, AutoType)])), VarDecl(UTB, ArrayType([6214533020, 0, 0, 205], StringType), BinExpr(::, BinExpr(||, Id(Y), Id(d)), BinExpr(>, Id(Br6), UnExpr(-, Id(w))))), VarDecl(SN, ArrayType([6214533020, 0, 0, 205], StringType), BinExpr(>, BinExpr(*, Id(kBDlJ0W), Id(H)), UnExpr(!, Id(Ep))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 554))

	def test_555(self):
		input = """v : function array [ 0 ] of string    ( ) { }    Z  : void  = 0    * d_jY3   - mqw5     || ! N   % I       :: e   + O1OD    - ! Pu     / Y       ;   """
		expect = """Program([
	FuncDecl(v, ArrayType([0], StringType), [], None, BlockStmt([]))
	VarDecl(Z, VoidType, BinExpr(::, BinExpr(||, BinExpr(-, BinExpr(*, IntegerLit(0), Id(d_jY3)), Id(mqw5)), BinExpr(%, UnExpr(!, Id(N)), Id(I))), BinExpr(-, BinExpr(+, Id(e), Id(O1OD)), BinExpr(/, UnExpr(!, Id(Pu)), Id(Y)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 555))

	def test_556(self):
		input = """ZAcqdD : function array [ 12 , 0 ] of float    ( out W : float     ) inherit z { break ;   }    u , N , VvFq_  : array [ 4_1 , 6 ] of integer    ;   y : function void  ( out JQ : void   , inherit r : void    ) { UDk  : float   ;  }    """
		expect = """Program([
	FuncDecl(ZAcqdD, ArrayType([12, 0], FloatType), [OutParam(W, FloatType)], z, BlockStmt([BreakStmt()]))
	VarDecl(u, ArrayType([41, 6], IntegerType))
	VarDecl(N, ArrayType([41, 6], IntegerType))
	VarDecl(VvFq_, ArrayType([41, 6], IntegerType))
	FuncDecl(y, VoidType, [OutParam(JQ, VoidType), InheritParam(r, VoidType)], None, BlockStmt([VarDecl(UDk, FloatType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 556))

	def test_557(self):
		input = """X : function auto  ( ) inherit IZz { s , C1L  : void  = 0    < ! _N     :: S   / c    > r   - HkP_eeiG      , K   / a       ;  }    """
		expect = """Program([
	FuncDecl(X, AutoType, [], IZz, BlockStmt([VarDecl(s, VoidType, BinExpr(::, BinExpr(<, IntegerLit(0), UnExpr(!, Id(_N))), BinExpr(>, BinExpr(/, Id(S), Id(c)), BinExpr(-, Id(r), Id(HkP_eeiG))))), VarDecl(C1L, VoidType, BinExpr(/, Id(K), Id(a)))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 557))

	def test_558(self):
		input = """dJ  : auto  ;   """
		expect = """Program([
	VarDecl(dJ, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 558))

	def test_559(self):
		input = """w  : void  ;   """
		expect = """Program([
	VarDecl(w, VoidType)
])"""
		self.assertTrue(TestAST.test(input, expect, 559))

	def test_560(self):
		input = """P9wJ : function array [ 6_11_25_6_79 , 0 , 3_1_1 , 33 , 0 , 83 ] of integer    ( ) { continue ;   }    N  : array [ 5620687914_8 , 19_79_916 ] of integer    = ! ! km   % b      <= o   - mRk    || tnLj   && kp     && rZ   && ZQ    * - aa         ;   """
		expect = """Program([
	FuncDecl(P9wJ, ArrayType([61125679, 0, 311, 33, 0, 83], IntegerType), [], None, BlockStmt([ContinueStmt()]))
	VarDecl(N, ArrayType([56206879148, 1979916], IntegerType), BinExpr(<=, BinExpr(%, UnExpr(!, UnExpr(!, Id(km))), Id(b)), BinExpr(&&, BinExpr(&&, BinExpr(&&, BinExpr(||, BinExpr(-, Id(o), Id(mRk)), Id(tnLj)), Id(kp)), Id(rZ)), BinExpr(*, Id(ZQ), UnExpr(-, Id(aa))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 560))

	def test_561(self):
		input = """D7b : function auto  ( ) inherit VIM3 { }    """
		expect = """Program([
	FuncDecl(D7b, AutoType, [], VIM3, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 561))

	def test_562(self):
		input = """Uc  : void  ;   """
		expect = """Program([
	VarDecl(Uc, VoidType)
])"""
		self.assertTrue(TestAST.test(input, expect, 562))

	def test_563(self):
		input = """f : function float   ( ) inherit t { for ( guO  = K   <= M   - FaJ8     :: sW   + Fm    > L   + Si      , ! Ib      , ZO0z   || v     :: ""    != ! oZ      ) break ;     }    """
		expect = """Program([
	FuncDecl(f, FloatType, [], t, BlockStmt([ForStmt(AssignStmt(Id(guO), BinExpr(::, BinExpr(<=, Id(K), BinExpr(-, Id(M), Id(FaJ8))), BinExpr(>, BinExpr(+, Id(sW), Id(Fm)), BinExpr(+, Id(L), Id(Si))))), UnExpr(!, Id(Ib)), BinExpr(::, BinExpr(||, Id(ZO0z), Id(v)), BinExpr(!=, StringLit(), UnExpr(!, Id(oZ)))), BreakStmt())]))
])"""
		self.assertTrue(TestAST.test(input, expect, 563))

	def test_564(self):
		input = """twV  : auto  ;   """
		expect = """Program([
	VarDecl(twV, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 564))

	def test_565(self):
		input = """X : function auto  ( inherit wKYlT9 : boolean     ) { }    """
		expect = """Program([
	FuncDecl(X, AutoType, [InheritParam(wKYlT9, BooleanType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 565))

	def test_566(self):
		input = """yv  : float   = ! - Lq      :: - O    % ""     / UdXC   || C    % i   || M      < sO   + ! - Ixf00pN         ;   Hz6eyH2  : string   = ! ! V    - QS   - ZjM      != t7s    :: - U    || - ki     - t   || BbQ9    - ! A      >= ! ! P     || uzeWwLt   + Qw    / H   || Twla         ;   """
		expect = """Program([
	VarDecl(yv, FloatType, BinExpr(::, UnExpr(!, UnExpr(-, Id(Lq))), BinExpr(<, BinExpr(||, BinExpr(||, BinExpr(/, BinExpr(%, UnExpr(-, Id(O)), StringLit()), Id(UdXC)), BinExpr(%, Id(C), Id(i))), Id(M)), BinExpr(+, Id(sO), UnExpr(!, UnExpr(-, Id(Ixf00pN)))))))
	VarDecl(Hz6eyH2, StringType, BinExpr(::, BinExpr(!=, BinExpr(-, BinExpr(-, UnExpr(!, UnExpr(!, Id(V))), Id(QS)), Id(ZjM)), Id(t7s)), BinExpr(>=, BinExpr(||, BinExpr(||, UnExpr(-, Id(U)), BinExpr(-, UnExpr(-, Id(ki)), Id(t))), BinExpr(-, Id(BbQ9), UnExpr(!, Id(A)))), BinExpr(||, BinExpr(||, UnExpr(!, UnExpr(!, Id(P))), BinExpr(+, Id(uzeWwLt), BinExpr(/, Id(Qw), Id(H)))), Id(Twla)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 566))

	def test_567(self):
		input = """Q : function auto  ( inherit P5q : void   , inherit out P : auto   , inherit X : boolean    , out Z7 : boolean     ) inherit T { }    izWz2 : function auto  ( ) { for ( n1gh  = - Z    < FBkT   || k     :: - oJ      , I   || lI4V    == L5FMiE8v   % mo5y     :: W   && gfb6      , Rb   && T      ) return ;     }    """
		expect = """Program([
	FuncDecl(Q, AutoType, [InheritParam(P5q, VoidType), InheritOutParam(P, AutoType), InheritParam(X, BooleanType), OutParam(Z7, BooleanType)], T, BlockStmt([]))
	FuncDecl(izWz2, AutoType, [], None, BlockStmt([ForStmt(AssignStmt(Id(n1gh), BinExpr(::, BinExpr(<, UnExpr(-, Id(Z)), BinExpr(||, Id(FBkT), Id(k))), UnExpr(-, Id(oJ)))), BinExpr(::, BinExpr(==, BinExpr(||, Id(I), Id(lI4V)), BinExpr(%, Id(L5FMiE8v), Id(mo5y))), BinExpr(&&, Id(W), Id(gfb6))), BinExpr(&&, Id(Rb), Id(T)), ReturnStmt())]))
])"""
		self.assertTrue(TestAST.test(input, expect, 567))

	def test_568(self):
		input = """Ar : function array [ 0 , 0 ] of boolean    ( Pr : auto   , mspDH : void   , inherit out z : auto    ) inherit j { return ;   }    """
		expect = """Program([
	FuncDecl(Ar, ArrayType([0, 0], BooleanType), [Param(Pr, AutoType), Param(mspDH, VoidType), InheritOutParam(z, AutoType)], j, BlockStmt([ReturnStmt()]))
])"""
		self.assertTrue(TestAST.test(input, expect, 568))

	def test_569(self):
		input = """t : function auto  ( out Gq : auto   , out T : boolean     ) { G6L  = WS ( )    > uY   % z      ;   }    """
		expect = """Program([
	FuncDecl(t, AutoType, [OutParam(Gq, AutoType), OutParam(T, BooleanType)], None, BlockStmt([AssignStmt(Id(G6L), BinExpr(>, FuncCall(WS, []), BinExpr(%, Id(uY), Id(z))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 569))

	def test_570(self):
		input = """X : function string   ( ) inherit LFGPTO5 { E , j  : auto  = r   || sD_     :: k ( )      , ! o8    <= ! p3YhB     :: ! cN    >= ! I       ;  EZ  : void  = O7   || sL       ;  }    Tv , C9j5  : void  ;   IjHzGC : function auto  ( inherit out uJi : auto   , inherit gt : void    ) inherit kb { O  = mg   || i    < - UX     :: 1    >= _y   + Q      ;   }    """
		expect = """Program([
	FuncDecl(X, StringType, [], LFGPTO5, BlockStmt([VarDecl(E, AutoType, BinExpr(::, BinExpr(||, Id(r), Id(sD_)), FuncCall(k, []))), VarDecl(j, AutoType, BinExpr(::, BinExpr(<=, UnExpr(!, Id(o8)), UnExpr(!, Id(p3YhB))), BinExpr(>=, UnExpr(!, Id(cN)), UnExpr(!, Id(I))))), VarDecl(EZ, VoidType, BinExpr(||, Id(O7), Id(sL)))]))
	VarDecl(Tv, VoidType)
	VarDecl(C9j5, VoidType)
	FuncDecl(IjHzGC, AutoType, [InheritOutParam(uJi, AutoType), InheritParam(gt, VoidType)], kb, BlockStmt([AssignStmt(Id(O), BinExpr(::, BinExpr(<, BinExpr(||, Id(mg), Id(i)), UnExpr(-, Id(UX))), BinExpr(>=, IntegerLit(1), BinExpr(+, Id(_y), Id(Q)))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 570))

	def test_571(self):
		input = """Kr , O , H  : string   ;   """
		expect = """Program([
	VarDecl(Kr, StringType)
	VarDecl(O, StringType)
	VarDecl(H, StringType)
])"""
		self.assertTrue(TestAST.test(input, expect, 571))

	def test_572(self):
		input = """vkaXX , o  : array [ 48_6_7_0_8_203_55 , 18 ] of string    = DhoInz33   && t    % - U   + Hw16      == - sr ( )       , { }     + ""    || orT4n   && T      >= - k37NcXCl ( )      :: x   + z    / kR8   * qk     * - d_   - S         ;   E50YWd : function auto  ( inherit out JV : void   , Jb : auto    ) inherit t { }    """
		expect = """Program([
	VarDecl(vkaXX, ArrayType([48670820355, 18], StringType), BinExpr(==, BinExpr(&&, Id(DhoInz33), BinExpr(+, BinExpr(%, Id(t), UnExpr(-, Id(U))), Id(Hw16))), UnExpr(-, FuncCall(sr, []))))
	VarDecl(o, ArrayType([48670820355, 18], StringType), BinExpr(::, BinExpr(>=, BinExpr(&&, BinExpr(||, BinExpr(+, ArrayLit([]), StringLit()), Id(orT4n)), Id(T)), UnExpr(-, FuncCall(k37NcXCl, []))), BinExpr(-, BinExpr(+, Id(x), BinExpr(*, BinExpr(*, BinExpr(/, Id(z), Id(kR8)), Id(qk)), UnExpr(-, Id(d_)))), Id(S))))
	FuncDecl(E50YWd, AutoType, [InheritOutParam(JV, VoidType), Param(Jb, AutoType)], t, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 572))

	def test_573(self):
		input = """_ , MDwU0IR  : void  ;   u9S  : void  = 0    || ! K    + - I       :: - Ckt    || - LMNLY     || Q ( )     < ! WkC    / ! Cm   * d         ;   Z  : void  = ! ! WTH     * - SO   || iR      >= - MS   || VHG    - - d       :: ! Lh_40   - Jpd    || - vfDYv         ;   """
		expect = """Program([
	VarDecl(_, VoidType)
	VarDecl(MDwU0IR, VoidType)
	VarDecl(u9S, VoidType, BinExpr(::, BinExpr(||, IntegerLit(0), BinExpr(+, UnExpr(!, Id(K)), UnExpr(-, Id(I)))), BinExpr(<, BinExpr(||, BinExpr(||, UnExpr(-, Id(Ckt)), UnExpr(-, Id(LMNLY))), FuncCall(Q, [])), BinExpr(*, BinExpr(/, UnExpr(!, Id(WkC)), UnExpr(!, Id(Cm))), Id(d)))))
	VarDecl(Z, VoidType, BinExpr(::, BinExpr(>=, BinExpr(||, BinExpr(*, UnExpr(!, UnExpr(!, Id(WTH))), UnExpr(-, Id(SO))), Id(iR)), BinExpr(||, UnExpr(-, Id(MS)), BinExpr(-, Id(VHG), UnExpr(-, Id(d))))), BinExpr(||, BinExpr(-, UnExpr(!, Id(Lh_40)), Id(Jpd)), UnExpr(-, Id(vfDYv)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 573))

	def test_574(self):
		input = """vk : function array [ 7_5120_0_9852 , 0 , 9_6 , 8 , 1129_61_92 ] of string    ( ) inherit LYo { n5 , P  : integer   ;  if ( O ( )     :: ! AFc      ) K ( )  ;   else return ;     break ;   p , v1Z0  : void  = 6    != ! _     :: ! Sx    <= - gX9      , ! n       ;  }    FQEMTN : function void  ( out _ : auto    ) { i  : boolean   ;  }    """
		expect = """Program([
	FuncDecl(vk, ArrayType([7512009852, 0, 96, 8, 11296192], StringType), [], LYo, BlockStmt([VarDecl(n5, IntegerType), VarDecl(P, IntegerType), IfStmt(BinExpr(::, FuncCall(O, []), UnExpr(!, Id(AFc))), CallStmt(K, ), ReturnStmt()), BreakStmt(), VarDecl(p, VoidType, BinExpr(::, BinExpr(!=, IntegerLit(6), UnExpr(!, Id(_))), BinExpr(<=, UnExpr(!, Id(Sx)), UnExpr(-, Id(gX9))))), VarDecl(v1Z0, VoidType, UnExpr(!, Id(n)))]))
	FuncDecl(FQEMTN, VoidType, [OutParam(_, AutoType)], None, BlockStmt([VarDecl(i, BooleanType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 574))

	def test_575(self):
		input = """UcY6_k : function void  ( inherit out oY : auto    ) inherit J { do { }  while ( ""     :: t_kpJp   + Ee      ) ;   k  : boolean   = Z   || m    == - kC       ;  }    """
		expect = """Program([
	FuncDecl(UcY6_k, VoidType, [InheritOutParam(oY, AutoType)], J, BlockStmt([DoWhileStmt(BinExpr(::, StringLit(), BinExpr(+, Id(t_kpJp), Id(Ee))), BlockStmt([])), VarDecl(k, BooleanType, BinExpr(==, BinExpr(||, Id(Z), Id(m)), UnExpr(-, Id(kC))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 575))

	def test_576(self):
		input = """I9UwIQ  : void  ;   """
		expect = """Program([
	VarDecl(I9UwIQ, VoidType)
])"""
		self.assertTrue(TestAST.test(input, expect, 576))

	def test_577(self):
		input = """s : function float   ( ) inherit KcIU2c { }    """
		expect = """Program([
	FuncDecl(s, FloatType, [], KcIU2c, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 577))

	def test_578(self):
		input = """s3ovLq , A , x7  : boolean   = ! - ImXe   % xK      != { }      :: - w1p2pv   * X1    * tH   % F      != - - eDCkEd     + s   || w    - ! a        , - - w   / WSGJSd        , o   + qUAW    || - r     + Z   && R    || ""      != p2d_Zqx ( )    % q   + pGghcglp     * - F   + z       :: - E    || - mg8     + C2   % V     != t   + h2    - M   && g     + true        ;   """
		expect = """Program([
	VarDecl(s3ovLq, BooleanType, BinExpr(::, BinExpr(!=, BinExpr(%, UnExpr(!, UnExpr(-, Id(ImXe))), Id(xK)), ArrayLit([])), BinExpr(!=, BinExpr(%, BinExpr(*, BinExpr(*, UnExpr(-, Id(w1p2pv)), Id(X1)), Id(tH)), Id(F)), BinExpr(||, BinExpr(+, UnExpr(-, UnExpr(-, Id(eDCkEd))), Id(s)), BinExpr(-, Id(w), UnExpr(!, Id(a)))))))
	VarDecl(A, BooleanType, BinExpr(/, UnExpr(-, UnExpr(-, Id(w))), Id(WSGJSd)))
	VarDecl(x7, BooleanType, BinExpr(::, BinExpr(!=, BinExpr(||, BinExpr(&&, BinExpr(||, BinExpr(+, Id(o), Id(qUAW)), BinExpr(+, UnExpr(-, Id(r)), Id(Z))), Id(R)), StringLit()), BinExpr(+, BinExpr(+, BinExpr(%, FuncCall(p2d_Zqx, []), Id(q)), BinExpr(*, Id(pGghcglp), UnExpr(-, Id(F)))), Id(z))), BinExpr(!=, BinExpr(||, UnExpr(-, Id(E)), BinExpr(+, UnExpr(-, Id(mg8)), BinExpr(%, Id(C2), Id(V)))), BinExpr(&&, BinExpr(-, BinExpr(+, Id(t), Id(h2)), Id(M)), BinExpr(+, Id(g), BooleanLit(True))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 578))

	def test_579(self):
		input = """B  : array [ 9704454 ] of boolean    ;   Q : function void  ( ) { }    ER : function auto  ( inherit out BS : array [ 0 ] of float      ) inherit X { }    """
		expect = """Program([
	VarDecl(B, ArrayType([9704454], BooleanType))
	FuncDecl(Q, VoidType, [], None, BlockStmt([]))
	FuncDecl(ER, AutoType, [InheritOutParam(BS, ArrayType([0], FloatType))], X, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 579))

	def test_580(self):
		input = """_  : array [ 0 , 0 , 0 ] of float    ;   """
		expect = """Program([
	VarDecl(_, ArrayType([0, 0, 0], FloatType))
])"""
		self.assertTrue(TestAST.test(input, expect, 580))

	def test_581(self):
		input = """ECb : function float   ( inherit IST : void   , d1 : auto   , out VV : auto   , O7 : array [ 2 , 4438 ] of integer     , inherit out aW : auto   , out aPbolL : string    , out S : float    , inherit A : auto    ) inherit GO { UCt  : void  ;  E , VU  : array [ 7533 ] of string    = - diRw    > g   % tkbU     :: c29mDs   * fNtO      , zb   || M       ;  }    """
		expect = """Program([
	FuncDecl(ECb, FloatType, [InheritParam(IST, VoidType), Param(d1, AutoType), OutParam(VV, AutoType), Param(O7, ArrayType([2, 4438], IntegerType)), InheritOutParam(aW, AutoType), OutParam(aPbolL, StringType), OutParam(S, FloatType), InheritParam(A, AutoType)], GO, BlockStmt([VarDecl(UCt, VoidType), VarDecl(E, ArrayType([7533], StringType), BinExpr(::, BinExpr(>, UnExpr(-, Id(diRw)), BinExpr(%, Id(g), Id(tkbU))), BinExpr(*, Id(c29mDs), Id(fNtO)))), VarDecl(VU, ArrayType([7533], StringType), BinExpr(||, Id(zb), Id(M)))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 581))

	def test_582(self):
		input = """i : function auto  ( ) { continue ;   }    g  : void  = true    == 0    || - WyO     / BU ( )    || Pz2   || h         ;   F  : array [ 6_2 ] of string    ;   """
		expect = """Program([
	FuncDecl(i, AutoType, [], None, BlockStmt([ContinueStmt()]))
	VarDecl(g, VoidType, BinExpr(==, BooleanLit(True), BinExpr(||, BinExpr(||, BinExpr(||, IntegerLit(0), BinExpr(/, UnExpr(-, Id(WyO)), FuncCall(BU, []))), Id(Pz2)), Id(h))))
	VarDecl(F, ArrayType([62], StringType))
])"""
		self.assertTrue(TestAST.test(input, expect, 582))

	def test_583(self):
		input = """I9UwIQ  : void  ;   """
		expect = """Program([
	VarDecl(I9UwIQ, VoidType)
])"""
		self.assertTrue(TestAST.test(input, expect, 583))

	def test_584(self):
		input = """ie , Prs  : auto  = - IQQ8WYV   + kSj     && ! m   || X      != - s3    || d   + Gt1kX     / - rv3    * n5   - _0cAJ4       :: - Pqz   + u7H     + true     < - HatyY   % w    || E       , B   != _   && wgFT    && - y     || ! vh   || d       :: - eY    - y8   || I     * ! oe5    && DoQ   + eR         ;   w1 , O_Z  : auto  = VZuayx   - q0JbX1s    && ! mIaq     + - U   || zO       :: rG   + a    && U_x   && w     + inNywn   - E    * n   / eYk      < - 0     / - N4    + r   * Vs        , U ( )       ;   """
		expect = """Program([
	VarDecl(ie, AutoType, BinExpr(::, BinExpr(!=, BinExpr(||, BinExpr(&&, BinExpr(+, UnExpr(-, Id(IQQ8WYV)), Id(kSj)), UnExpr(!, Id(m))), Id(X)), BinExpr(||, UnExpr(-, Id(s3)), BinExpr(-, BinExpr(+, Id(d), BinExpr(*, BinExpr(/, Id(Gt1kX), UnExpr(-, Id(rv3))), Id(n5))), Id(_0cAJ4)))), BinExpr(<, BinExpr(+, BinExpr(+, UnExpr(-, Id(Pqz)), Id(u7H)), BooleanLit(True)), BinExpr(||, BinExpr(%, UnExpr(-, Id(HatyY)), Id(w)), Id(E)))))
	VarDecl(Prs, AutoType, BinExpr(::, BinExpr(!=, Id(B), BinExpr(||, BinExpr(||, BinExpr(&&, BinExpr(&&, Id(_), Id(wgFT)), UnExpr(-, Id(y))), UnExpr(!, Id(vh))), Id(d))), BinExpr(&&, BinExpr(||, BinExpr(-, UnExpr(-, Id(eY)), Id(y8)), BinExpr(*, Id(I), UnExpr(!, Id(oe5)))), BinExpr(+, Id(DoQ), Id(eR)))))
	VarDecl(w1, AutoType, BinExpr(::, BinExpr(||, BinExpr(&&, BinExpr(-, Id(VZuayx), Id(q0JbX1s)), BinExpr(+, UnExpr(!, Id(mIaq)), UnExpr(-, Id(U)))), Id(zO)), BinExpr(<, BinExpr(&&, BinExpr(&&, BinExpr(+, Id(rG), Id(a)), Id(U_x)), BinExpr(-, BinExpr(+, Id(w), Id(inNywn)), BinExpr(/, BinExpr(*, Id(E), Id(n)), Id(eYk)))), BinExpr(+, BinExpr(/, UnExpr(-, IntegerLit(0)), UnExpr(-, Id(N4))), BinExpr(*, Id(r), Id(Vs))))))
	VarDecl(O_Z, AutoType, FuncCall(U, []))
])"""
		self.assertTrue(TestAST.test(input, expect, 584))

	def test_585(self):
		input = """n : function auto  ( inherit out o : boolean    , out O : array [ 0 , 0 , 525 ] of boolean      ) inherit N { }    _ : function auto  ( inherit out s3F : boolean     ) inherit R { }    """
		expect = """Program([
	FuncDecl(n, AutoType, [InheritOutParam(o, BooleanType), OutParam(O, ArrayType([0, 0, 525], BooleanType))], N, BlockStmt([]))
	FuncDecl(_, AutoType, [InheritOutParam(s3F, BooleanType)], R, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 585))

	def test_586(self):
		input = """Es : function array [ 69 ] of string    ( ) inherit W { oiM , t  : void  = ! rSu    == ! DX      , ! k    == e   - ZB       ;  }    l3KvwH  : array [ 0 ] of integer    ;   v : function void  ( i : integer     ) inherit b { }    """
		expect = """Program([
	FuncDecl(Es, ArrayType([69], StringType), [], W, BlockStmt([VarDecl(oiM, VoidType, BinExpr(==, UnExpr(!, Id(rSu)), UnExpr(!, Id(DX)))), VarDecl(t, VoidType, BinExpr(==, UnExpr(!, Id(k)), BinExpr(-, Id(e), Id(ZB))))]))
	VarDecl(l3KvwH, ArrayType([0], IntegerType))
	FuncDecl(v, VoidType, [Param(i, IntegerType)], b, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 586))

	def test_587(self):
		input = """F7jD : function float   ( ) inherit AUj4 { }    s , Xsv  : array [ 732_65 , 87_2 , 15_6 ] of integer    ;   ziHv : function integer   ( inherit out qj : array [ 0 ] of string      ) inherit pW { }    """
		expect = """Program([
	FuncDecl(F7jD, FloatType, [], AUj4, BlockStmt([]))
	VarDecl(s, ArrayType([73265, 872, 156], IntegerType))
	VarDecl(Xsv, ArrayType([73265, 872, 156], IntegerType))
	FuncDecl(ziHv, IntegerType, [InheritOutParam(qj, ArrayType([0], StringType))], pW, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 587))

	def test_588(self):
		input = """lh  : array [ 598 ] of integer    ;   """
		expect = """Program([
	VarDecl(lh, ArrayType([598], IntegerType))
])"""
		self.assertTrue(TestAST.test(input, expect, 588))

	def test_589(self):
		input = """dB : function boolean   ( ) { if ( J   && e      ) continue ;   else { }     }    xU : function void  ( out s86Aq6 : array [ 4 ] of integer      ) { Irb ( )  ;   GE8hN  : auto  = 0    < z   * S       ;  }    """
		expect = """Program([
	FuncDecl(dB, BooleanType, [], None, BlockStmt([IfStmt(BinExpr(&&, Id(J), Id(e)), ContinueStmt(), BlockStmt([]))]))
	FuncDecl(xU, VoidType, [OutParam(s86Aq6, ArrayType([4], IntegerType))], None, BlockStmt([CallStmt(Irb, ), VarDecl(GE8hN, AutoType, BinExpr(<, IntegerLit(0), BinExpr(*, Id(z), Id(S))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 589))

	def test_590(self):
		input = """e13h , Fu , evk  : auto  ;   """
		expect = """Program([
	VarDecl(e13h, AutoType)
	VarDecl(Fu, AutoType)
	VarDecl(evk, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 590))

	def test_591(self):
		input = """W  : array [ 0 , 0 ] of string    = qz ( )    <= false    + 0      :: W   / L    + - P     % j   / n    % ! G         ;   """
		expect = """Program([
	VarDecl(W, ArrayType([0, 0], StringType), BinExpr(::, BinExpr(<=, FuncCall(qz, []), BinExpr(+, BooleanLit(False), IntegerLit(0))), BinExpr(+, BinExpr(/, Id(W), Id(L)), BinExpr(%, BinExpr(/, BinExpr(%, UnExpr(-, Id(P)), Id(j)), Id(n)), UnExpr(!, Id(G))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 591))

	def test_592(self):
		input = """h , RR  : array [ 9 , 1628 ] of float    ;   """
		expect = """Program([
	VarDecl(h, ArrayType([9, 1628], FloatType))
	VarDecl(RR, ArrayType([9, 1628], FloatType))
])"""
		self.assertTrue(TestAST.test(input, expect, 592))

	def test_593(self):
		input = """cq : function array [ 0 ] of integer    ( inherit dT4 : auto   , out C : boolean    , v0 : array [ 3 ] of boolean     , out Y : auto    ) inherit jERd { { }   }    t : function auto  ( inherit W : array [ 2 ] of boolean      ) inherit Vc { }    """
		expect = """Program([
	FuncDecl(cq, ArrayType([0], IntegerType), [InheritParam(dT4, AutoType), OutParam(C, BooleanType), Param(v0, ArrayType([3], BooleanType)), OutParam(Y, AutoType)], jERd, BlockStmt([BlockStmt([])]))
	FuncDecl(t, AutoType, [InheritParam(W, ArrayType([2], BooleanType))], Vc, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 593))

	def test_594(self):
		input = """cq : function array [ 0 ] of integer    ( inherit dT4 : auto   , out C : boolean    , v0 : array [ 3 ] of boolean     , out Y : auto    ) inherit jERd { { }   }    t : function auto  ( inherit W : array [ 2 ] of boolean      ) inherit Vc { }    """
		expect = """Program([
	FuncDecl(cq, ArrayType([0], IntegerType), [InheritParam(dT4, AutoType), OutParam(C, BooleanType), Param(v0, ArrayType([3], BooleanType)), OutParam(Y, AutoType)], jERd, BlockStmt([BlockStmt([])]))
	FuncDecl(t, AutoType, [InheritParam(W, ArrayType([2], BooleanType))], Vc, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 594))

	def test_595(self):
		input = """I  : void  = ! oIO   - R     + A   * i    && zOrS   - vu       :: Pa   - U    * y   && M1     && uSQ   / GmV    % ! Pb3         ;   """
		expect = """Program([
	VarDecl(I, VoidType, BinExpr(::, BinExpr(&&, BinExpr(+, BinExpr(-, UnExpr(!, Id(oIO)), Id(R)), BinExpr(*, Id(A), Id(i))), BinExpr(-, Id(zOrS), Id(vu))), BinExpr(&&, BinExpr(&&, BinExpr(-, Id(Pa), BinExpr(*, Id(U), Id(y))), Id(M1)), BinExpr(%, BinExpr(/, Id(uSQ), Id(GmV)), UnExpr(!, Id(Pb3))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 595))
	
	def test_596(self):
		input = """iM  : float   = false    >= ! S   + jB     || - ""       :: E85r   * ea0J    / _ ( )     % ! X ( )      > - O   && Cn1M     + { }         ;   Y : function void  ( ) { R , g  : auto  = v23   || x     :: ""      , x8   % n     :: WLX   <= - b       ;  return ;   }    T : function auto  ( inherit v4s : auto    ) { while ( t    :: - wTtkn      ) { }     }    """
		expect = """Program([
	VarDecl(iM, FloatType, BinExpr(::, BinExpr(>=, BooleanLit(False), BinExpr(||, BinExpr(+, UnExpr(!, Id(S)), Id(jB)), UnExpr(-, StringLit()))), BinExpr(>, BinExpr(%, BinExpr(/, BinExpr(*, Id(E85r), Id(ea0J)), FuncCall(_, [])), UnExpr(!, FuncCall(X, []))), BinExpr(&&, UnExpr(-, Id(O)), BinExpr(+, Id(Cn1M), ArrayLit([]))))))
	FuncDecl(Y, VoidType, [], None, BlockStmt([VarDecl(R, AutoType, BinExpr(::, BinExpr(||, Id(v23), Id(x)), StringLit())), VarDecl(g, AutoType, BinExpr(::, BinExpr(%, Id(x8), Id(n)), BinExpr(<=, Id(WLX), UnExpr(-, Id(b))))), ReturnStmt()]))
	FuncDecl(T, AutoType, [InheritParam(v4s, AutoType)], None, BlockStmt([WhileStmt(BinExpr(::, Id(t), UnExpr(-, Id(wTtkn))), BlockStmt([]))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 596))

	def test_597(self):
		input = """iM  : float   = false    >= ! S   + jB     || - ""       :: E85r   * ea0J    / _ ( )     % ! X ( )      > - O   && Cn1M     + { }         ;   Y : function void  ( ) { R , g  : auto  = v23   || x     :: ""      , x8   % n     :: WLX   <= - b       ;  return ;   }    T : function auto  ( inherit v4s : auto    ) { while ( t    :: - wTtkn      ) { }     }    """
		expect = """Program([
	VarDecl(iM, FloatType, BinExpr(::, BinExpr(>=, BooleanLit(False), BinExpr(||, BinExpr(+, UnExpr(!, Id(S)), Id(jB)), UnExpr(-, StringLit()))), BinExpr(>, BinExpr(%, BinExpr(/, BinExpr(*, Id(E85r), Id(ea0J)), FuncCall(_, [])), UnExpr(!, FuncCall(X, []))), BinExpr(&&, UnExpr(-, Id(O)), BinExpr(+, Id(Cn1M), ArrayLit([]))))))
	FuncDecl(Y, VoidType, [], None, BlockStmt([VarDecl(R, AutoType, BinExpr(::, BinExpr(||, Id(v23), Id(x)), StringLit())), VarDecl(g, AutoType, BinExpr(::, BinExpr(%, Id(x8), Id(n)), BinExpr(<=, Id(WLX), UnExpr(-, Id(b))))), ReturnStmt()]))
	FuncDecl(T, AutoType, [InheritParam(v4s, AutoType)], None, BlockStmt([WhileStmt(BinExpr(::, Id(t), UnExpr(-, Id(wTtkn))), BlockStmt([]))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 597))

	def test_598(self):
		input = """f  : auto  ;   """
		expect = """Program([
	VarDecl(f, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 598))

	def test_599(self):
		input = """NHPm : function array [ 92_4 , 336227233 , 0 , 24252_7 , 0 ] of boolean    ( ) inherit js48 { Wt  : array [ 0 , 0 ] of string    ;  }    f  : auto  ;   RE  : void  ;   NmZ  : array [ 0 , 0 , 0 ] of float    ;   H  : void  = ! ! j    + Zo   || oWK         ;   Wd : function auto  ( inherit EC : void    ) inherit l { Jh29  : boolean   = g   - T9FT    > P3   || Ar     :: a   || o       ;  fgFDX  : integer   = j   % mDteu    < - B       ;  }    x , w  : array [ 0 , 54 , 0 ] of boolean    = ! ! drHA     + R   || CM    % fW   && IX       :: ! - t   * LaI        , gv   / J    % b ( )     * ! J9    % kJ   % AdO         ;   """
		expect = """Program([
	FuncDecl(NHPm, ArrayType([924, 336227233, 0, 242527, 0], BooleanType), [], js48, BlockStmt([VarDecl(Wt, ArrayType([0, 0], StringType))]))
	VarDecl(f, AutoType)
	VarDecl(RE, VoidType)
	VarDecl(NmZ, ArrayType([0, 0, 0], FloatType))
	VarDecl(H, VoidType, BinExpr(||, BinExpr(+, UnExpr(!, UnExpr(!, Id(j))), Id(Zo)), Id(oWK)))
	FuncDecl(Wd, AutoType, [InheritParam(EC, VoidType)], l, BlockStmt([VarDecl(Jh29, BooleanType, BinExpr(::, BinExpr(>, BinExpr(-, Id(g), Id(T9FT)), BinExpr(||, Id(P3), Id(Ar))), BinExpr(||, Id(a), Id(o)))), VarDecl(fgFDX, IntegerType, BinExpr(<, BinExpr(%, Id(j), Id(mDteu)), UnExpr(-, Id(B))))]))
	VarDecl(x, ArrayType([0, 54, 0], BooleanType), BinExpr(::, BinExpr(&&, BinExpr(||, BinExpr(+, UnExpr(!, UnExpr(!, Id(drHA))), Id(R)), BinExpr(%, Id(CM), Id(fW))), Id(IX)), BinExpr(*, UnExpr(!, UnExpr(-, Id(t))), Id(LaI))))
	VarDecl(w, ArrayType([0, 54, 0], BooleanType), BinExpr(%, BinExpr(%, BinExpr(*, BinExpr(%, BinExpr(/, Id(gv), Id(J)), FuncCall(b, [])), UnExpr(!, Id(J9))), Id(kJ)), Id(AdO)))
])"""
		self.assertTrue(TestAST.test(input, expect, 599))

	def test_600(self):
		input = """Yc : function auto  ( inherit out ZtS : integer    , out I : auto    ) inherit KTb { }    W : function auto  ( ) { G  : array [ 0 , 0 , 0 , 2 , 0 , 9 ] of string    = P   || Mq    <= g   - D6jS       ;  _dV , z6  : auto  = bh   || tDom     :: W   - ls    < P9   - g3      , - RazXiT    == q   || Ia       ;  while ( duM   && Yxl     :: KPA0 ( )    <= z   + hEg      ) break ;     continue ;   return ;   }    """
		expect = """Program([
	FuncDecl(Yc, AutoType, [InheritOutParam(ZtS, IntegerType), OutParam(I, AutoType)], KTb, BlockStmt([]))
	FuncDecl(W, AutoType, [], None, BlockStmt([VarDecl(G, ArrayType([0, 0, 0, 2, 0, 9], StringType), BinExpr(<=, BinExpr(||, Id(P), Id(Mq)), BinExpr(-, Id(g), Id(D6jS)))), VarDecl(_dV, AutoType, BinExpr(::, BinExpr(||, Id(bh), Id(tDom)), BinExpr(<, BinExpr(-, Id(W), Id(ls)), BinExpr(-, Id(P9), Id(g3))))), VarDecl(z6, AutoType, BinExpr(==, UnExpr(-, Id(RazXiT)), BinExpr(||, Id(q), Id(Ia)))), WhileStmt(BinExpr(::, BinExpr(&&, Id(duM), Id(Yxl)), BinExpr(<=, FuncCall(KPA0, []), BinExpr(+, Id(z), Id(hEg)))), BreakStmt()), ContinueStmt(), ReturnStmt()]))
])"""
		self.assertTrue(TestAST.test(input, expect, 600))
	