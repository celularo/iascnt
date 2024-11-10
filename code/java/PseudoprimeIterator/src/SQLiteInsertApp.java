import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class SQLiteInsertApp {
    private Connection conn;

    public SQLiteInsertApp(Connection conny) {
        this.conn = conny;
    }

    public void insert_into_table(String tab, Long key, Long val, String source, String base, Long bound) {
        String sql = "INSERT INTO tab(key,val,source,base,bound) VALUES(?,?,?,?,?)";
        sql = sql.replace("tab", tab);

        try (
                PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setLong(1, key);
            pstmt.setLong(2, val);
            pstmt.setString(3, source);
            pstmt.setString(4, base);
            pstmt.setLong(5, bound);

            pstmt.executeUpdate();
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }

    public void insert_spsp_into_table(String tab, Long key, String source, SPSPDataOnSQLite spsp) {
        String sql = "INSERT INTO tab(key,val,source,base,core,abs_depth,core_modpow,succ_depth)" +
                " VALUES(?,?,?,?,?,?,?,?)";
        sql = sql.replace("tab", tab);

        try (
                PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setLong(1, key);
            pstmt.setLong(2, spsp.val);
            pstmt.setString(3, source);
            pstmt.setLong(4, spsp.base);
            pstmt.setLong(5, spsp.core);
            pstmt.setLong(6, spsp.absDepth);
            pstmt.setLong(7, spsp.coreModPow);
            pstmt.setLong(8, spsp.succDepth);


            pstmt.executeUpdate();
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }
}
